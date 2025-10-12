import pygame, sys, random, time
from pygame.locals import *
from assets import *
from player import Player
from enemy import Enemy
from coin import Coin1, Coin2
from blast import Blast
from utils import draw_text, draw_lives, load_high_score, save_high_score

pygame.init()
pygame.mixer.init()
FPS = 60
FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Harry Potter Game")

# Load sounds
pygame.mixer.music.load("assets/game_bg.wav")
pygame.mixer.music.play(-1)
point_sound = pygame.mixer.Sound('assets/point.wav')
blast_sound = pygame.mixer.Sound('assets/blast.wav')

# Game state
SCORE = 0
HIGHEST_SCORE = load_high_score()
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
            # ...draw start page text/images...
        if event.type == pygame.KEYDOWN:
            if game_state == "start_page":
                game_state = "playing"
        if game_state == "playing":
            if event.type == INC_SPEED:
                SPEED += 0.1
                if SPEED > MAX_SPEED:
                    SPEED = MAX_SPEED
    if game_state == "playing":
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)
        DISPLAYSURF.blit(background, (0, 0))
        all_sprites.draw(DISPLAYSURF)
        draw_text(DISPLAYSURF, str(SCORE), 30, 30, 10)
        draw_lives(DISPLAYSURF, 800, 10, P1.lives, live_bar)
        all_sprites.update()
        # ...collision and scoring logic...
        if P1.lives == 0:
            game_state = "game_over"
    elif game_state == "game_over":
        for enemy in enemies:
            enemy.kill()
        # ...game over screen...
        pygame.display.update()
        time.sleep(6)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)
