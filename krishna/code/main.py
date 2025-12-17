import pygame
from random import randint
import os
from os.path import join


def space_game(root):

    # ================= PATHS =================
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    SPRITES = join(BASE_DIR, "sprites")
    AUDIO = join(BASE_DIR, "audio")

    # ================= INIT =================
    pygame.init()
    w, h = 1280, 720
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Space Monkey")
    clock = pygame.time.Clock()

    # ================= LOAD ASSETS =================
    player_surf = pygame.image.load(join(SPRITES, "player.png")).convert_alpha()
    meteor_surf = pygame.image.load(join(SPRITES, "meteor.png")).convert_alpha()
    laser_surf = pygame.image.load(join(SPRITES, "laser.png")).convert_alpha()
    font_big = pygame.font.Font(join(SPRITES, "Oxanium-Bold.ttf"), 60)
    font_small = pygame.font.Font(join(SPRITES, "Oxanium-Bold.ttf"), 35)

    explosion_frames = [
        pygame.image.load(join(SPRITES, "explosion", f"{i}.png")).convert_alpha()
        for i in range(21)
    ]

    laser_sound = pygame.mixer.Sound(join(AUDIO, "laser.wav"))
    explosion_sound = pygame.mixer.Sound(join(AUDIO, "explosion.wav"))
    damage_sound = pygame.mixer.Sound(join(AUDIO, "damage.ogg"))
    game_music = pygame.mixer.Sound(join(AUDIO, "game_music2.mp3"))

    # ================= MENUS =================
    def start_menu():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); return False

            screen.fill((20, 20, 30))
            title = font_big.render("SPACE MONKEY", True, (255, 255, 255))
            start = font_small.render("Press ENTER to Start", True, (200, 200, 200))
            exit_ = font_small.render("Press ESC to Exit", True, (200, 200, 200))

            screen.blit(title, title.get_rect(center=(w//2, h//2 - 80)))
            screen.blit(start, start.get_rect(center=(w//2, h//2)))
            screen.blit(exit_, exit_.get_rect(center=(w//2, h//2 + 50)))

            pygame.display.update()

    def end_menu(score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); return False

            screen.fill((20, 20, 30))
            score_txt = font_big.render(f"Score: {score}", True, (255, 255, 255))
            replay = font_small.render("ENTER to Play Again", True, (200, 200, 200))
            exit_ = font_small.render("ESC to Exit", True, (200, 200, 200))

            screen.blit(score_txt, score_txt.get_rect(center=(w//2, h//2 - 50)))
            screen.blit(replay, replay.get_rect(center=(w//2, h//2 + 20)))
            screen.blit(exit_, exit_.get_rect(center=(w//2, h//2 + 60)))

            pygame.display.update()

    # ================= GAME LOOP =================
    while True:

        if not start_menu():
            return

        # groups
        all_sprites = pygame.sprite.Group()
        meteor_sprites = pygame.sprite.Group()
        laser_sprites = pygame.sprite.Group()

        class Player(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(all_sprites)
                self.image = player_surf
                self.rect = self.image.get_rect(center=(w//2, h//2))
                self.pos = pygame.Vector2(self.rect.center)
                self.speed = 300
                self.last_shot = 0
                self.mask = pygame.mask.from_surface(self.image)

            def update(self, dt):
                keys = pygame.key.get_pressed()
                direction = pygame.Vector2(
                    keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                    keys[pygame.K_DOWN] - keys[pygame.K_UP]
                )

                if direction:
                    self.pos += direction.normalize() * self.speed * dt
                    self.rect.center = self.pos

                self.rect.clamp_ip(screen.get_rect())
                self.pos = pygame.Vector2(self.rect.center)

                if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shot > 400:
                    Laser(self.rect.midtop)
                    laser_sound.play()
                    self.last_shot = pygame.time.get_ticks()

        class Laser(pygame.sprite.Sprite):
            def __init__(self, pos):
                super().__init__(all_sprites, laser_sprites)
                self.image = laser_surf
                self.rect = self.image.get_rect(midbottom=pos)
                self.mask = pygame.mask.from_surface(self.image)

            def update(self, dt):
                self.rect.y -= 500 * dt
                if self.rect.bottom < 0:
                    self.kill()

        class Meteor(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(all_sprites, meteor_sprites)
                self.image = meteor_surf
                self.rect = self.image.get_rect(center=(randint(0, w), -40))
                self.speed = randint(200, 400)
                self.mask = pygame.mask.from_surface(self.image)

            def update(self, dt):
                self.rect.y += self.speed * dt
                if self.rect.top > h:
                    self.kill()

        class Explosion(pygame.sprite.Sprite):
            def __init__(self, pos):
                super().__init__(all_sprites)
                self.frames = explosion_frames
                self.index = 0
                self.image = self.frames[0]
                self.rect = self.image.get_rect(center=pos)

            def update(self, dt):
                self.index += 20 * dt
                if self.index < len(self.frames):
                    self.image = self.frames[int(self.index)]
                else:
                    self.kill()

        player = Player()
        game_music.play(loops=-1)

        meteor_event = pygame.USEREVENT
        pygame.time.set_timer(meteor_event, 700)

        start_time = pygame.time.get_ticks()
        running = True

        while running:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); return
                if event.type == meteor_event:
                    Meteor()

            if pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask):
                damage_sound.play()
                running = False

            for laser in laser_sprites:
                hits = pygame.sprite.spritecollide(laser, meteor_sprites, True, pygame.sprite.collide_mask)
                if hits:
                    laser.kill()
                    Explosion(laser.rect.center)
                    explosion_sound.play()

            all_sprites.update(dt)

            screen.fill((15, 15, 30))
            all_sprites.draw(screen)
            pygame.display.update()

        game_music.stop()
        score = (pygame.time.get_ticks() - start_time) // 1000

        if not end_menu(score):
            return
