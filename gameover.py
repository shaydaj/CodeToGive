import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)


background_image = pygame.image.load('16b18df7-a231-48ff-8db0-59441ddec1a0.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


play_image = pygame.image.load('gameover.png')
play_button_image = pygame.transform.scale(play_image, (500, 400))

options_image = pygame.image.load('playagain.png')
options_button_image = pygame.transform.scale(options_image, (330, 250))

play_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 - 230 , 400, 300)
options_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 , 330, 200)


running = True
while running:
    screen.blit(background_image, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play_button_rect.collidepoint(mouse_pos):
         screen.blit(pygame.transform.scale(play_image, (530, 420)), play_button_rect.move(-15, -10))
    else:
        screen.blit(play_button_image, play_button_rect)

    if options_button_rect.collidepoint(mouse_pos):
        screen.blit(pygame.transform.scale(options_image, (350, 270)), options_button_rect.move(-10, -5))
    else:
        screen.blit(options_button_image, options_button_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
