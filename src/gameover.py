import pygame
import sys
import main


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)

background_image = pygame.image.load("src/assets/images/endingbackground.jpg")
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

gameover = pygame.image.load("src/assets/images/gameover.png")
gameoverimage = pygame.transform.scale(gameover, (575, 175))
gameover_rect = gameoverimage.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
)

playagain = pygame.image.load("src/assets/images/playagainbutton.png")
playagainimage = pygame.transform.scale(playagain, (200, 100))

playagainrect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 320, 120)


def new_screen():
    main.main()


running = True
while running:
    screen.blit(background_image, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(gameoverimage, gameover_rect)

    if playagainrect.collidepoint(mouse_pos):
        screen.blit(
            pygame.transform.scale(playagainimage, (220, 120)),
            playagainrect.move(-10, -5),
        )
    else:
        screen.blit(playagainimage, playagainrect)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if playagainrect.collidepoint(mouse_pos):
            new_screen()

    pygame.display.flip()

pygame.quit()
sys.exit()
