import pygame
from pygame.locals import *
from src.assets import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/assets/potter.png")
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.center = (100, 160)
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 10)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (100, 160)
