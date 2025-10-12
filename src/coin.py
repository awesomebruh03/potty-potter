import pygame
import random
from src.assets import WIDTH, HEIGHT

class Coin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/assets/coin.png")
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))

    def move(self, speed):
        self.rect.move_ip(-1.25*speed, 0)
        if self.rect.left < 10:
            self.rect.right = WIDTH
            self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/assets/coin.png")
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))

    def move(self, speed):
        self.rect.move_ip(-1.25*speed, 0)
        if self.rect.left < 10:
            self.rect.right = WIDTH
            self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))
