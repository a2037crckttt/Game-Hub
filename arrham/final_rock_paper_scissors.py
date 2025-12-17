import pygame
import random
import os



def rock_paper(root):
    pygame.init()
    pygame.mixer.init()

    win = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Rock Paper Scissors")

    emoji_font = pygame.font.SysFont("Segoe UI Emoji", 110)
    text_font = pygame.font.Font(None, 48)
    big_text_font = pygame.font.Font(None, 58)

    white = (255, 255, 255)
    dark_blue = (5, 5, 40)

    emojis = {1: "✌", 2: "✊", 3: "✋"}

    # background stars
    stars = [(random.randint(0, 1000), random.randint(0, 600), random.randint(1, 2)) for _ in range(70)]

    # -------- SOUND (same folder) --------
    BASE_DIR = os.path.dirname(__file__)
    music_path = os.path.join(BASE_DIR, "game_music.wav")

    bg_music = pygame.mixer.Sound(music_path)
    bg_music.play(loops=-1)


    # optional sounds (won't crash if missing)
    try:
        click_sound = pygame.mixer.Sound("click.wav")
    except:
        click_sound = None

    try:
        win_sound = pygame.mixer.Sound("win.wav")
    except:
        win_sound = None

    try:
        lose_sound = pygame.mixer.Sound("lose.wav")
    except:
        lose_sound = None

    player_choice = None
    computer_choice = None
    result = ""

    wins = losses = draws = 0

    animating = False
    anim_timer = 0
    bounce_y = 0

    clock = pygame.time.Clock()
    run = True

    # ================= MAIN LOOP =================
    while run:
        clock.tick(20)

        win.fill(dark_blue)
        for sx, sy, sr in stars:
            pygame.draw.circle(win, white, (sx, sy), sr)

        win.blit(text_font.render("Press 1 Scissors | 2 Rock | 3 Paper", True, white), (200, 50))
        score_text = f"Wins: {wins}   Losses: {losses}   Draws: {draws}"
        win.blit(big_text_font.render(score_text, True, white), (200, 100))

        # ---------- ANIMATION ----------
        if player_choice is not None and not animating and result == "":
            animating = True
            anim_timer = 0
            bounce_y = 0

        if animating:
            anim_timer += 1
            bounce_y = -18 if (anim_timer // 5) % 2 == 0 else 0

            win.blit(emoji_font.render(emojis[player_choice], True, white), (300, 250 + bounce_y))
            win.blit(emoji_font.render(emojis[random.randint(1, 3)], True, white), (500, 250 + bounce_y))

            if anim_timer >= 36:
                animating = False
                anim_timer = 0
                bounce_y = 0

                computer_choice = random.randint(1, 3)

                if player_choice == computer_choice:
                    result = "Draw"
                    draws += 1
                elif (player_choice, computer_choice) in [(1, 3), (2, 1), (3, 2)]:
                    result = "You Won"
                    wins += 1
                    if win_sound:
                        win_sound.play()
                else:
                    result = "You Lost"
                    losses += 1
                    if lose_sound:
                        lose_sound.play()

        else:
            if player_choice is not None:
                win.blit(emoji_font.render(emojis[player_choice], True, white), (300, 250))
            if computer_choice is not None:
                win.blit(emoji_font.render(emojis[computer_choice], True, white), (500, 250))
            if result:
                win.blit(big_text_font.render(result, True, white), (400, 400))

        pygame.display.update()

        # ---------- EVENTS ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bg_music.stop()
                pygame.quit()
                return   # back to launcher

            if event.type == pygame.KEYDOWN:
                if click_sound:
                    click_sound.play()

                if event.key == pygame.K_SPACE:
                    player_choice = computer_choice = None
                    result = ""
                    animating = False
                    anim_timer = 0
                    bounce_y = 0

                if animating:
                    continue

                if event.key == pygame.K_1:
                    player_choice = 1
                    result = ""
                    computer_choice = None
                elif event.key == pygame.K_2:
                    player_choice = 2
                    result = ""
                    computer_choice = None
                elif event.key == pygame.K_3:
                    player_choice = 3
                    result = ""
                    computer_choice = None
