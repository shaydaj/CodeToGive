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
font = pygame.font.Font('assets/fonts/8-BIT WONDER.TTF', 30)

# Set up display
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("Game")

# Define relative coordinates based on DISPLAY_W and DISPLAY_H
settings_popup_border = pygame.Rect(0.25 * DISPLAY_W, 0.25 * DISPLAY_H, 0.5 * DISPLAY_W, 0.5 * DISPLAY_H)
settings_popup_rect = pygame.Rect(0.25 * DISPLAY_W + 5, 0.25 * DISPLAY_H + 5, 0.5 * DISPLAY_W - 10, 0.5 * DISPLAY_H - 10)
close_button_rect = pygame.Rect(0.44 * DISPLAY_W, 0.67 * DISPLAY_H, 0.12 * DISPLAY_W, 0.07 * DISPLAY_H)

# Settings
audio_on = False
visual_guide_on = False
vibration_on = False
game_speed = 5

def draw_text(text, size, colour, x, y, return_rect=False):
    font = pygame.font.Font('assets/fonts/8-BIT WONDER.TTF', size) 
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    if return_rect:
        return textrect

def home_screen():
    background = pygame.image.load('assets/images/background.jpg')
    start_button_image = pygame.image.load('assets/images/button.png')
    settings_button_image = pygame.image.load('assets/images/button.png')

    start_button_rect = start_button_image.get_rect()
    settings_button_rect = settings_button_image.get_rect()

    start_button_rect.topleft = (DISPLAY_W / 2 - start_button_rect.width / 2, DISPLAY_H / 2 - 200)
    settings_button_rect.topleft = (DISPLAY_W / 2 - settings_button_rect.width / 2, DISPLAY_H / 2 + 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return
                elif settings_button_rect.collidepoint(event.pos):
                    show_settings_popup()

        screen.blit(background, (0, 0))
        screen.blit(start_button_image, start_button_rect)
        screen.blit(settings_button_image, settings_button_rect)

        draw_text("Start Game", 25, WHITE, start_button_rect.x + 40, start_button_rect.y + 60)
        draw_text("Settings", 25, WHITE, settings_button_rect.x + 60, settings_button_rect.y + 60)

        pygame.display.update()


def show_settings_popup():
    audio_toggle_rect = pygame.Rect(0.625 * DISPLAY_W, 0.33 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H)
    visual_toggle_rect = pygame.Rect(0.625 * DISPLAY_W, 0.41 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H)
    vibration_toggle_rect = pygame.Rect(0.625 * DISPLAY_W, 0.49 * DISPLAY_H, 0.07 * DISPLAY_W, 0.04 * DISPLAY_H)
    speed_slider_rect = pygame.Rect(0.375 * DISPLAY_W, 0.63 * DISPLAY_H, 0.25 * DISPLAY_W, 0.0167 * DISPLAY_H)

    global audio_on, visual_guide_on, vibration_on, game_speed

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
                if vibration_toggle_rect.collidepoint(event.pos):
                    vibration_on = not vibration_on
                if speed_slider_rect.collidepoint(event.pos):
                    game_speed = int((event.pos[0] - speed_slider_rect.left) / (speed_slider_rect.width - 10) * 10)
                    game_speed = min(max(game_speed, 0), 10)

        pygame.draw.rect(screen, WHITE, settings_popup_border)
        pygame.draw.rect(screen, BLACK, settings_popup_rect)
        
        pygame.draw.rect(screen, BLACK, close_button_rect)
        draw_text("Close", 20, WHITE, close_button_rect.x + 10, close_button_rect.y + 10)

        draw_text("Audio Prompts", 20, WHITE, settings_popup_rect.x + 50, audio_toggle_rect.y)
        draw_text("Visual Guide", 20, WHITE, settings_popup_rect.x + 50, visual_toggle_rect.y)
        draw_text("Vibration", 20, WHITE, settings_popup_rect.x + 50, vibration_toggle_rect.y)
        draw_text("Game Speed", 20, WHITE, settings_popup_rect.x + 130, speed_slider_rect.y - 40)

        pygame.draw.rect(screen, WHITE, audio_toggle_rect)
        draw_text("On" if audio_on else "Off", 20, BLACK, audio_toggle_rect.x + 5, audio_toggle_rect.y + 5)

        pygame.draw.rect(screen, WHITE, visual_toggle_rect)
        draw_text("On" if visual_guide_on else "Off", 20, BLACK, visual_toggle_rect.x + 5, visual_toggle_rect.y + 5)

        pygame.draw.rect(screen, WHITE, vibration_toggle_rect)
        draw_text("On" if vibration_on else "Off", 20, BLACK, vibration_toggle_rect.x + 5, vibration_toggle_rect.y + 5)

        pygame.draw.rect(screen, WHITE, speed_slider_rect)
        slider_handle_x = speed_slider_rect.left + int(game_speed / 10 * (speed_slider_rect.width)) 
        slider_handle_rect = pygame.Rect(slider_handle_x, speed_slider_rect.top - 5, 10, 25)
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
