import pygame
import sys
import game

# Initialize Pygame
pygame.init()

# Set up sizes, fonts and colors
DISPLAY_W = 960
DISPLAY_H = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)

font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 30)

PINK = (235,84,76)

font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 30)


# Set up display
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("Concrete Jungle, Climbing Challenge")

# Define relative coordinates based on DISPLAY_W and DISPLAY_H
settings_popup_border = pygame.Rect(
    0.25 * DISPLAY_W, 0.2 * DISPLAY_H, 0.5 * DISPLAY_W, 0.65 * DISPLAY_H
)
settings_popup_rect = pygame.Rect(
    0.25 * DISPLAY_W + 5,
    0.2 * DISPLAY_H + 5,
    0.5 * DISPLAY_W - 10,
    0.65 * DISPLAY_H - 10,
)
close_button_rect = pygame.Rect(
    0.44 * DISPLAY_W, 0.77 * DISPLAY_H, 0.12 * DISPLAY_W, 0.07 * DISPLAY_H
)

# Settings
audio_on = False
visual_guide_on = False
shake_to_move_on = False
voice_controls_on = False
simple_background_on = False
game_speed = 5

slider_dragging = False


def display_title():

    title_image = pygame.image.load(
        "assets/images/gametitle.png"
    )  # Replace "path/to/your/title.png" with the actual file path

    scaled_title_image = pygame.transform.scale(title_image, (600, 225))
    title_rect = scaled_title_image.get_rect(center=(DISPLAY_W // 2, 275))  # Adjust the y-coordinate (here 30) for vertical positioning
    screen.blit(scaled_title_image, title_rect)

def draw_text(text, size, colour, x, y, return_rect=False):
    font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", size)
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    if return_rect:
        return textrect


def home_screen():
    background = pygame.image.load("assets/images/background2.jpg")
    start_button_image = pygame.image.load("assets/images/startgamebutton.png")
    settings_button_image = pygame.image.load("assets/images/optionsbutton.png")
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 100

    start_button_image = pygame.transform.scale(start_button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
    settings_button_image = pygame.transform.scale(settings_button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

    start_button_rect = start_button_image.get_rect()
    settings_button_rect = settings_button_image.get_rect()

    start_button_rect.topleft = (
        DISPLAY_W // 2 - start_button_rect.width // 2,
        DISPLAY_H // 2 + 60,
    )
    settings_button_rect.topleft = (
        DISPLAY_W // 2 - settings_button_rect.width // 2,
        DISPLAY_H // 2 + 150,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button_rect.collidepoint(event.pos):
                    show_settings_popup()
                if start_button_rect.collidepoint(event.pos):
                        selected_character = character_selection_popup()
                        if selected_character is not None:
                            return selected_character

        screen.blit(background, (0, 0))
        screen.blit(start_button_image, start_button_rect)
        screen.blit(settings_button_image, settings_button_rect)
        display_title()


        pygame.display.update()

def character_selection_popup():

    character_popup_border = pygame.Rect(
        0.2 * DISPLAY_W, 
        0.15 * DISPLAY_H,
        0.6 * DISPLAY_W, 
        0.8 * DISPLAY_H
    )
    character_popup_rect = pygame.Rect(
        0.2 * DISPLAY_W + 5,
        0.15 * DISPLAY_H + 5,
        0.6 * DISPLAY_W - 10,
        0.8 * DISPLAY_H - 10,
    )

    gorilla_button_rect = pygame.Rect(
            0.3 * DISPLAY_W,
            0.37 * DISPLAY_H,
            0.25 * DISPLAY_W,
            0.25 * DISPLAY_H  
        )
    rabbit_button_rect = pygame.Rect(
            0.17 * DISPLAY_W,
            0.63 * DISPLAY_H,  
            0.25 * DISPLAY_W,
            0.25 * DISPLAY_H  
        )
    cat_button_rect = pygame.Rect(
            0.45 * DISPLAY_W,  
            0.38 * DISPLAY_H,
            0.25 * DISPLAY_W,
            0.25 * DISPLAY_H 
        )
    duck_button_rect = pygame.Rect(
            0.45 * DISPLAY_W,  
            0.65 * DISPLAY_H,  
            0.25 * DISPLAY_W,
            0.25 * DISPLAY_H 
        )
    
    selected_character = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
    
                if gorilla_button_rect.collidepoint(event.pos):
                    selected_character = 1
                elif rabbit_button_rect.collidepoint(event.pos):
                    selected_character = 2
                elif cat_button_rect.collidepoint(event.pos):  # Added cat button event
                    selected_character = 3
                elif duck_button_rect.collidepoint(event.pos):  # Added duck button event
                    selected_character = 4

        if selected_character is not None:
            return selected_character

        pygame.draw.rect(screen, WHITE, character_popup_border)
        pygame.draw.rect(screen, PINK, character_popup_rect)

        select_character_image = pygame.image.load('src/assets/images/players.jpeg')

        screen.blit(select_character_image, (character_popup_rect.x + 120, character_popup_rect.y + 20))

        gorilla_image = pygame.image.load('src/assets/images/gorilla.png')
        gorilla_image = pygame.transform.scale(gorilla_image, (200, 200))
        screen.blit(gorilla_image, (gorilla_button_rect.x, gorilla_button_rect.y))

        rabbit_image = pygame.image.load('src/assets/images/rabbit.png')
        rabbit_image = pygame.transform.scale(rabbit_image, (450, 200))
        screen.blit(rabbit_image, (rabbit_button_rect.x, rabbit_button_rect.y))

        cat_image = pygame.image.load('src/assets/images/cat.png')
        cat_image = pygame.transform.scale(cat_image, (350, 250))
        screen.blit(cat_image, (cat_button_rect.x, cat_button_rect.y))

        duck_image = pygame.image.load('src/assets/images/duck.png')
        duck_image = pygame.transform.scale(duck_image, (350, 200))
        screen.blit(duck_image, (duck_button_rect.x, duck_button_rect.y))

        pygame.display.update()





def show_settings_popup():
    global slider_dragging

    audio_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.25 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    visual_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.33 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    shake_to_move_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.41 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    voice_controls_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.49 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    simple_background_toggle_rect = pygame.Rect(
        0.625 * DISPLAY_W, 0.57 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H
    )
    speed_slider_rect = pygame.Rect(
        0.375 * DISPLAY_W, 0.72 * DISPLAY_H, 0.25 * DISPLAY_W, 0.0167 * DISPLAY_H
    )

    global audio_on, visual_guide_on, shake_to_move_on, voice_controls_on, simple_background_on, game_speed

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
                if simple_background_toggle_rect.collidepoint(event.pos):
                    simple_background_on = not simple_background_on
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
            "Audio Prompts", 18, WHITE, settings_popup_rect.x + 50, audio_toggle_rect.y
        )
        draw_text(
            "Visual Guide", 18, WHITE, settings_popup_rect.x + 50, visual_toggle_rect.y
        )
        draw_text(
            "Shake to Move", 18, WHITE, settings_popup_rect.x + 50, shake_to_move_toggle_rect.y
        )
        draw_text(
            "Voice Controls", 18, WHITE, settings_popup_rect.x + 50, voice_controls_toggle_rect.y
        )
        draw_text(
            "Simple Backgroud", 18, WHITE, settings_popup_rect.x + 50, simple_background_toggle_rect.y
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

        pygame.draw.rect(screen, WHITE, simple_background_toggle_rect)
        draw_text(
            "On" if simple_background_on else "Off",
            20,
            BLACK,
            simple_background_toggle_rect.x + 5,
            simple_background_toggle_rect.y + 5,
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


def game_screen(character):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_settings_popup()

        screen.fill(WHITE)

        draw_text(f"Selected Character {character}", 30, BLACK, DISPLAY_W//2 - 300, DISPLAY_H//2)

        pygame.display.update()


def main():
    character = home_screen()
    game.game_running(visual_guide_on, game_speed)


if __name__ == "__main__":
    main()
