import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up sizes, fonts and colors
DISPLAY_W = 960
DISPLAY_H = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
font = pygame.font.Font("src/assets/fonts/8-BIT WONDER.TTF", 30)

# Set up display
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("Game")

# Define relative coordinates based on DISPLAY_W and DISPLAY_H
settings_popup_border = pygame.Rect(
    0.25 * DISPLAY_W, 0.25 * DISPLAY_H, 0.5 * DISPLAY_W, 0.6 * DISPLAY_H
)
settings_popup_rect = pygame.Rect(
    0.25 * DISPLAY_W + 5,
    0.25 * DISPLAY_H + 5,
    0.5 * DISPLAY_W - 10,
    0.6 * DISPLAY_H - 10,
)
close_button_rect = pygame.Rect(
    0.44 * DISPLAY_W, 0.77 * DISPLAY_H, 0.12 * DISPLAY_W, 0.07 * DISPLAY_H
)

# Settings
audio_on = False
visual_guide_on = False
shake_to_move_on = False
voice_controls_on = False
game_speed = 5

slider_dragging = False

def draw_text(text, size, colour, x, y, return_rect=False):
    font = pygame.font.Font("src/assets/fonts/8-BIT WONDER.TTF", size)
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    if return_rect:
        return textrect


def home_screen():
    background = pygame.image.load("src/assets/images/background2.jpg")
    start_button_image = pygame.image.load("src/assets/images/startgamebutton.png")
    settings_button_image = pygame.image.load("src/assets/images/optionsbutton.png")

    start_button_rect = start_button_image.get_rect()
    settings_button_rect = settings_button_image.get_rect()

    start_button_rect.topleft = (
        DISPLAY_W / 2 - start_button_rect.width / 2,
        DISPLAY_H / 2 - 100,
    )
    settings_button_rect.topleft = (
        DISPLAY_W / 2 - settings_button_rect.width / 2,
        DISPLAY_H / 2 ,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button_rect.collidepoint(event.pos):
                    show_settings_popup()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return

        screen.blit(background, (0, 0))
        screen.blit(start_button_image, start_button_rect)
        screen.blit(settings_button_image, settings_button_rect)


        pygame.display.update()


def show_settings_popup():
    global slider_dragging

    audio_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.33 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    visual_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.41 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    shake_to_move_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.49 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    voice_controls_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.57 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    speed_slider_rect = pygame.Rect(
        0.375 * DISPLAY_W, 0.71 * DISPLAY_H, 0.25 * DISPLAY_W, 0.0167 * DISPLAY_H
    )

    global audio_on, visual_guide_on, shake_to_move_on, voice_controls_on, game_speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button_rect.collidepoint(event.pos):
                    return
                if audio_toggle_rect.collidepoint(event.pos):
                    audio_on = not audio_on
                if visual_toggle_rect.collidepoint(event.pos):
                    visual_guide_on = not visual_guide_on
                if shake_to_move_toggle_rect.collidepoint(event.pos):
                    shake_to_move_on = not shake_to_move_on
                    voice_controls_on = False
                if voice_controls_toggle_rect.collidepoint(event.pos):
                    voice_controls_on = not voice_controls_on
                    shake_to_move_on = False
                if speed_slider_rect.collidepoint(event.pos):
                    slider_dragging = True  # Start dragging the slider
            if event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False  # Stop dragging the slider
            if event.type == pygame.MOUSEMOTION:
                if slider_dragging:
                    # Update game speed based on mouse position
                    game_speed = (event.pos[0] - speed_slider_rect.left) / (speed_slider_rect.width - 10) * 10
                    game_speed = min(max(game_speed, 0), 10)

        pygame.draw.rect(screen, WHITE, settings_popup_border)
        pygame.draw.rect(screen, BLACK, settings_popup_rect)

        pygame.draw.rect(screen, BLACK, close_button_rect)
        draw_text(
            "Close", 20, WHITE, close_button_rect.x + 10, close_button_rect.y + 10
        )

        draw_text(
            "Audio Prompts", 20, WHITE, settings_popup_rect.x + 50, audio_toggle_rect.y
        )
        draw_text(
            "Visual Guide", 20, WHITE, settings_popup_rect.x + 50, visual_toggle_rect.y
        )
        draw_text(
            "Shake to Move", 20, WHITE, settings_popup_rect.x + 50, shake_to_move_toggle_rect.y
        )
        draw_text(
            "Voice Controls", 20, WHITE, settings_popup_rect.x + 50, voice_controls_toggle_rect.y
        )
        draw_text(
            "Game Speed",
            20,
            WHITE,
            settings_popup_rect.x + 130,
            speed_slider_rect.y - 40,
        )

        pygame.draw.rect(screen, WHITE, audio_toggle_rect)
        draw_text(
            "On" if audio_on else "Off",
            20,
            BLACK,
            audio_toggle_rect.x + 5,
            audio_toggle_rect.y + 5,
        )

        pygame.draw.rect(screen, WHITE, visual_toggle_rect)
        draw_text(
            "On" if visual_guide_on else "Off",
            20,
            BLACK,
            visual_toggle_rect.x + 5,
            visual_toggle_rect.y + 5,
        )

        pygame.draw.rect(screen, WHITE, shake_to_move_toggle_rect)
        draw_text(
            "On" if shake_to_move_on else "Off",
            20,
            BLACK,
            shake_to_move_toggle_rect.x + 5,
            shake_to_move_toggle_rect.y + 5,
        )

        pygame.draw.rect(screen, WHITE, voice_controls_toggle_rect)
        draw_text(
            "On" if voice_controls_on else "Off",
            20,
            BLACK,
            voice_controls_toggle_rect.x + 5,
            voice_controls_toggle_rect.y + 5,
        )

        pygame.draw.rect(screen, WHITE, speed_slider_rect)
        slider_handle_x = speed_slider_rect.left + int(
            game_speed / 10 * (speed_slider_rect.width)
        )
        slider_handle_rect = pygame.Rect(
            slider_handle_x, speed_slider_rect.top - 5, 15, 25
        )
        pygame.draw.rect(screen, GREY, slider_handle_rect)

        pygame.display.update()


def game_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_settings_popup()

        screen.fill(WHITE)
        pygame.display.update()


def main():
    home_screen()
    game_screen()


if __name__ == "__main__":
    main()
