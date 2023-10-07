import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)


background_image = pygame.image.load('assets/images/endingbackground.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


play_image = pygame.image.load('assets/images/gameoverbutton.png')
play_button_image = pygame.transform.scale(play_image, (300, 100))

options_image = pygame.image.load('assets/images/playagainbutton.png')
options_button_image = pygame.transform.scale(options_image, (200, 100))

play_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 320, 120)
options_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50 , 220, 120)


running = True
while running:
    screen.blit(background_image, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play_button_rect.collidepoint(mouse_pos):
         screen.blit(pygame.transform.scale(play_image, (320, 120)), play_button_rect.move(-10, -5))
    else:
        screen.blit(play_button_image, play_button_rect)

    if options_button_rect.collidepoint(mouse_pos):
        screen.blit(pygame.transform.scale(options_image, (220, 120)), options_button_rect.move(-10, -5))
    else:
        screen.blit(options_button_image, options_button_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
