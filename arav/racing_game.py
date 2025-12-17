import pygame
import math
import os
from sys import exit

# Main Screen
def car_game(root):
    pygame.init()
    clock = pygame.time.Clock()
    screen_main = pygame.display.set_mode((1300,650))
    pygame.display.set_caption("FORMULA1_BIHARI _VERSION")

    BASE_DIR = os.path.dirname(__file__)

    race_suraface = pygame.image.load(
        os.path.join(BASE_DIR, "racetrack.png")
    )
    race_suraface = pygame.transform.smoothscale(race_suraface,(1300,650))

    FINISH_X = 670
    game_over = False
    winner = ""
    font = pygame.font.Font(None, 150)

    vector = pygame.math.Vector2

    class Track(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load(
                os.path.join(BASE_DIR, "e.png")
            ).convert_alpha()
            self.rect = self.image.get_rect(center=(x,y))
        
    class start(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.already_ran = False
            self.sprite_animate = False
            self.sprite_list = []

            self.timer_empty = pygame.image.load(
                os.path.join(BASE_DIR, "empty.png")
            ).convert_alpha()
            self.timer_3 = pygame.image.load(
                os.path.join(BASE_DIR, "3.png")
            ).convert_alpha()
            self.timer_2 = pygame.image.load(
                os.path.join(BASE_DIR, "2.png")
            ).convert_alpha()
            self.timer_1 = pygame.image.load(
                os.path.join(BASE_DIR, "1.png")
            ).convert_alpha()
            self.timer_GO = pygame.image.load(
                os.path.join(BASE_DIR, "GO.png")
            ).convert_alpha()

            self.sprite_list.append(self.timer_empty)
            self.sprite_list.append(self.timer_3)
            self.sprite_list.append(self.timer_2)
            self.sprite_list.append(self.timer_1)
            self.sprite_list.append(self.timer_GO)

            self.current_sprite = 0
            self.image = self.sprite_list[int(self.current_sprite)]
            self.rect = self.image.get_rect(center=(x, y))

        def animate(self):
            keys = pygame.key.get_pressed()
            if not self.already_ran and keys[pygame.K_SPACE]:
                self.sprite_animate = True
                self.already_ran = True    

        def update(self):
            if self.sprite_animate == True:
                self.current_sprite += 0.03
                if self.current_sprite >= len(self.sprite_list):
                    self.current_sprite = 0
                    self.sprite_animate = False
            self.image = self.sprite_list[int(self.current_sprite)]

    class Car_1(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.already_ran_car1 = False
            self.original_image = pygame.image.load(
                os.path.join(BASE_DIR, "Car_1.png")
            ).convert_alpha()
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(x, y))

            self.angle = 0
            self.speed_front = 10 
            self.speed_back = 5
            self.position = vector(x, y)
            self.laps = 0
            self.was_left = True 

        def update(self):
            nonlocal game_over, winner
            keys = pygame.key.get_pressed()

            if game_over:
                text_surface = font.render(winner, True, (255,255,255))
                text_rect = text_surface.get_rect(center=(650, 325))
                screen_main.blit(text_surface, text_rect)
                return

            if keys[pygame.K_SPACE]:
                self.already_ran_car1 = True

            if self.already_ran_car1 == True:
                if keys[pygame.K_RIGHT]:
                    self.angle -= 4
                if keys[pygame.K_LEFT]:
                    self.angle += 4

                rad = math.radians(self.angle)

                if keys[pygame.K_UP]:
                    self.position.x += self.speed_front * math.cos(rad)
                    self.position.y -= self.speed_front * math.sin(rad)

                if keys[pygame.K_DOWN]:
                    self.position.x -= self.speed_back * math.cos(rad)
                    self.position.y += self.speed_back * math.sin(rad)

                self.rect.center = self.position
                self.image = pygame.transform.rotate(self.original_image, self.angle)
                self.rect = self.image.get_rect(center=self.rect.center)

                if self.position.x > 1260:
                    self.position.x = 1260
                elif self.position.y > 600:
                    self.position.y = 600
                elif self.position.x < 50:
                    self.position.x = 50
                elif self.position.y < 45:
                    self.position.y = 45

                if pygame.sprite.spritecollide(self, track_group, False, pygame.sprite.collide_mask):
                    self.speed_front = 0
                    self.speed_back = 0.5
                else:
                    self.speed_front = 10
                    self.speed_back = 5

                is_left = self.rect.centerx < FINISH_X
                if self.was_left and not is_left:
                    self.laps += 1
                    if self.laps == 6:
                        winner = "RED WINS"
                        game_over = True
                self.was_left = is_left
            
    class Car_2(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.already_ran_car2 = False
            self.original_image = pygame.image.load(
                os.path.join(BASE_DIR, "Car_2.png")
            ).convert_alpha()
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(x, y))

            self.angle = 0
            self.speed_front = 10
            self.speed_back = 5
            self.position = vector(x, y)
            self.laps = 0
            self.was_left = True

        def update(self):
            nonlocal game_over, winner
            keys = pygame.key.get_pressed()

            if game_over:
                text_surface = font.render(winner, True, (255,255,255))
                text_rect = text_surface.get_rect(center=(650, 325))
                screen_main.blit(text_surface, text_rect)
                return

            if keys[pygame.K_SPACE]:
                self.already_ran_car2 = True
            
            if self.already_ran_car2 == True:
                if keys[pygame.K_d]:
                    self.angle -= 4
                if keys[pygame.K_a]:
                    self.angle += 4

                rad = math.radians(self.angle)

                if keys[pygame.K_w]:
                    self.position.x += self.speed_front * math.cos(rad)
                    self.position.y -= self.speed_front * math.sin(rad)

                if keys[pygame.K_s]:
                    self.position.x -= self.speed_back * math.cos(rad)
                    self.position.y += self.speed_back * math.sin(rad)

                self.rect.center = self.position
                self.image = pygame.transform.rotate(self.original_image, self.angle)
                self.rect = self.image.get_rect(center=self.rect.center)

                if self.position.x > 1260:
                    self.position.x = 1260
                elif self.position.y > 600:
                    self.position.y = 600
                elif self.position.x < 50:
                    self.position.x = 50
                elif self.position.y < 45:
                    self.position.y = 45

                if pygame.sprite.spritecollide(self, track_group, False, pygame.sprite.collide_mask):
                    self.speed_front = 0
                    self.speed_back = 0.5
                else:
                    self.speed_front = 10
                    self.speed_back = 5

                is_left = self.rect.centerx < FINISH_X
                if self.was_left and not is_left:
                    self.laps += 1
                    if self.laps == 6:
                        winner = "BLUE WINS"
                        game_over = True
                self.was_left = is_left
                        
    car1_group = pygame.sprite.Group()
    car1_group.add(Car_1(550,530))

    car2_group = pygame.sprite.Group()
    car2_group.add(Car_2(550,490))

    timer_group = pygame.sprite.Group()
    timer = start(525,225)
    timer_group.add(timer)

    track_group = pygame.sprite.Group()
    track_group.add(Track(650,308))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                timer.animate()

        screen_main.blit(race_suraface,(0,0))
        timer_group.update()
        timer_group.draw(screen_main)
        car1_group.update()
        car1_group.draw(screen_main)
        car2_group.update()
        car2_group.draw(screen_main)

        pygame.display.update()
        clock.tick(60)
