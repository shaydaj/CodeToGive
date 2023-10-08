import pygame
import sys
import main
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)

background_image = pygame.image.load("assets/images/endingbackground.jpg")
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load other images and set up rectangles as you did before...

banana_image = pygame.image.load('assets/images/Individual Banana.png')
banana_image = pygame.transform.scale(banana_image, (40, 40))
clock = pygame.time.Clock()

bananas = []
for _ in range(5):
    banana_x = random.randint(0, SCREEN_WIDTH - banana_image.get_width())
    banana_y = random.randint(-100, -10)
    banana_speed_y = random.randint(1, 5)
    bananas.append([banana_x, banana_y, banana_speed_y])

# Game loop
running = True

background_image = pygame.image.load("assets/images/endingbackground.jpg")
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

gameover = pygame.image.load("assets/images/gameover.png")
gameoverimage = pygame.transform.scale(gameover, (700, 175))
gameover_rect = gameoverimage.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
)

gameover1 = pygame.image.load("assets/images/gameover1.png")
gameoverimage1 = pygame.transform.scale(gameover1, (400, 400))
gameover_rect1 = gameoverimage1.get_rect(
    center=(SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2 + 175)
)



playagain = pygame.image.load("assets/images/playagainbutton.png")
playagainimage = pygame.transform.scale(playagain, (200, 100))
playagainrect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 90, 320, 120)



def new_screen():
    main.main()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bananas
    for banana in bananas:
        banana[1] += banana[2]
        if banana[1] > SCREEN_HEIGHT:
            banana[1] = random.randint(-100, -10)
            banana[0] = random.randint(0, SCREEN_WIDTH - banana_image.get_width())

    # Clear the screen by filling it with the background image
    screen.blit(background_image, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    # Draw bananas
    for banana in bananas:
        screen.blit(banana_image, (banana[0], banana[1]))

    # Draw game over images and buttons
    screen.blit(gameoverimage, gameover_rect)
    screen.blit(gameoverimage1, gameover_rect1)

    if playagainrect.collidepoint(pygame.mouse.get_pos()):
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
    clock.tick(60)


pygame.quit()
sys.exit()
