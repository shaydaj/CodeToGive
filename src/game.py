import random

import pygame
import time
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        self.count = 0
        player_walk_1 = scalePlayer("src/assets/images/gorilla-1.png")
        player_walk_2 = scalePlayer("src/assets/images/gorilla-2.png")

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = scalePlayer("assets/images/gorilla-1.png")

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(550, 500))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.right >= 550:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.x += self.gravity
        if self.rect.right >= 550:
            self.rect.right = 550

    def animation_state(self):
        if self.rect.right < 550:
            self.image = self.player_jump

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
    
    def get_banana_count(self):
        return self.count

    def add_banana_count(self):
        self.count += 1


class Food(pygame.sprite.Sprite):
    def __init__(self, foodtype):
        super().__init__()
        if foodtype == 1:
            banana_1 = scaleFood("assets/images/banana.png")
            self.image = banana_1

        elif foodtype == 2:
            banana_2 = scaleFood("assets/images/banana.png")
            self.image = banana_2

        elif foodtype == 3:
            banana_3 = scaleFood("assets/images/banana.png")
            self.image = banana_3

        elif foodtype == 4:
            banana_4 = scaleFood("assets/images/banana.png")
            self.image = banana_4

        y_pos = 10
        self.rect = self.image.get_rect(midbottom=(300, y_pos))

    def update(self, GAME_SPEED):
        self.rect.y += 1 * GAME_SPEED
        self.destroy()

    def destroy(self):
        if self.rect.y >= 500:
            self.kill()


def collision_sprite(player, food_group):
    if pygame.sprite.spritecollide(player.sprite, food_group, False):
        return 1
    else:
        return 0


def scalePlayer(path):
    bg_img = pygame.image.load(path).convert_alpha()
    bg_image = pygame.transform.scale(bg_img, (int(width // 8), int(height // 7)))
    return bg_image


def scaleFood(path):
    bg_img = pygame.image.load(path).convert_alpha()
    bg_image = pygame.transform.scale(bg_img, (int(width // 15), int(height // 15)))
    return bg_image


# pygame.init()
width = 960
height = 720


def game_running(PAUSE_NEED, x, screen, sound):
    GAME_SPEED = x
    PAUSE = 0
    if PAUSE_NEED:
        PAUSE = 2
    window = pygame.display.set_mode((width, height))
    bg_img = pygame.image.load("assets/images/tower.png")
    bg_img = pygame.transform.scale(bg_img, (int(width // 2), height))
    beautiful_bg = [
        "assets/images/Daylight skyline.png",
        "assets/images/ny night 3.png",
    ]
    if not screen:
        bg_img1 = pygame.image.load(random.choice(beautiful_bg))
    else:
        bg_img1 = pygame.image.load("src/assets/images/white_screen.jpg")
    bg_img1 = pygame.transform.scale(bg_img1, (int(width // 2), height))
    game_width = int(width // 2)
    i = 0

    character = Player()
    player = pygame.sprite.GroupSingle()
    player.add(character)

    food_group = pygame.sprite.Group()

    food_timer = pygame.USEREVENT + 1
    running = True

    pygame.mixer.music.load("assets/audios/chill.mp3")

    if sound:
        pygame.mixer.music.play(-1)
    pygame.time.set_timer(food_timer, int(10000 // (GAME_SPEED + 1)))
    clock = pygame.time.Clock()
    active = True
    added = False

    while running:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == food_timer and active:
                food_group.add(Food(random.choice([1, 1, 1, 2, 2, 2, 3, 3, 4, 4])))
                added = True

        window.blit(bg_img1, (0, 0))
        window.blit(bg_img, (game_width, i))
        window.blit(bg_img, (game_width, i - height))

        if added:
            pygame.time.delay(PAUSE * 1000)
            active = False
            added = False
            i += 1

        else:
            active = True
            if i >= height:
                window.blit(bg_img, (game_width, height))
                i = 0
            i += GAME_SPEED + 1

            if collision_sprite(player, food_group):
                food_group.remove(food_group.sprites()[0])
                character.add_banana_count()

            banana_img = pygame.image.load("src/assets/images/banana.png")
            banana_img = pygame.transform.scale(banana_img, (150, 100))  # Adjust the size as needed
            window.blit(banana_img, (0, 0))  # Display banana at (10, 10)
            font = pygame.font.Font('src/assets/fonts/8-BIT WONDER.TTF', 36)
            count_text = font.render(str(character.get_banana_count()), True, (76, 187, 23))
            window.blit(count_text, (120, 40)) 

            player.draw(window)
            player.update()

            food_group.draw(window)
            food_group.update((GAME_SPEED + 1))
            pygame.display.update()
            clock.tick(60)


pygame.quit()
