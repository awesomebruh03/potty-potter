
import sys
sys.path.insert(0, './src')

import pygame, random, time
from pygame.locals import *
from src.assets import WIDTH, HEIGHT, background, live_bar, MAX_SPEED
from src.player import Player
from src.enemy import Enemy
from src.coin import Coin1, Coin2
from src.blast import Blast
from src.utils import draw_text, draw_lives, load_high_score, save_high_score

pygame.init()
pygame.mixer.init()
FPS = 60
FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Harry Potter Game")

# Load sounds
pygame.mixer.music.load("src/assets/game_bg.wav")
pygame.mixer.music.play(-1)
point_sound = pygame.mixer.Sound('src/assets/point.wav')
blast_sound = pygame.mixer.Sound('src/assets/blast.wav')

# Game state
SCORE = 0
HIGHEST_SCORE = load_high_score()
SPEED = 10
game_state = "start_page"

# Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin1()
C2 = Coin2()
enemies = pygame.sprite.Group(E1)
coins1 = pygame.sprite.Group(C1)
coins2 = pygame.sprite.Group(C2)
all_sprites = pygame.sprite.Group(P1, E1, C1, C2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if game_state == "start_page":
            DISPLAYSURF.blit(background, (0, 0))
            draw_text(DISPLAYSURF, "The Harry Potter Game", 64, WIDTH / 2, HEIGHT / 4)
            draw_text(DISPLAYSURF, "Press any key to begin", 22, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        waiting = False
                        game_state = "playing"

        if game_state == "playing":
            if event.type == INC_SPEED:
                SPEED += 0.1
                if SPEED > MAX_SPEED:
                    SPEED = MAX_SPEED

    if game_state == "playing":
        DISPLAYSURF.blit(background, (0, 0))

        for entity in all_sprites:
            if isinstance(entity, Enemy):
                entity.move(SPEED, lambda points: globals().__setitem__('SCORE', SCORE + points))
            elif isinstance(entity, (Coin1, Coin2)):
                entity.move(SPEED)
            else:
                entity.move()

        # Check for collisions
        if pygame.sprite.spritecollide(P1, enemies, True, pygame.sprite.collide_circle):
            P1.lives -= 1
            blast_sound.play()
            E1 = Enemy()
            enemies.add(E1)
            all_sprites.add(E1)

        if pygame.sprite.spritecollide(P1, coins1, True, pygame.sprite.collide_circle):
            SCORE += 1
            point_sound.play()
            C1 = Coin1()
            coins1.add(C1)
            all_sprites.add(C1)

        if pygame.sprite.spritecollide(P1, coins2, True, pygame.sprite.collide_circle):
            SCORE += 1
            point_sound.play()
            C2 = Coin2()
            coins2.add(C2)
            all_sprites.add(C2)

        all_sprites.draw(DISPLAYSURF)
        draw_text(DISPLAYSURF, str(SCORE), 30, 30, 10)
        draw_lives(DISPLAYSURF, 800, 10, P1.lives, live_bar)

        if P1.lives == 0:
            game_state = "game_over"

    elif game_state == "game_over":
        for enemy in enemies:
            enemy.kill()
        # ...game over screen...
        draw_text(DISPLAYSURF, "Game Over", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(DISPLAYSURF, f"Score: {SCORE}", 22, WIDTH / 2, HEIGHT / 2)
        draw_text(DISPLAYSURF, f"High Score: {HIGHEST_SCORE}", 22, WIDTH/2, HEIGHT/2+40)
        pygame.display.flip()
        time.sleep(6)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
