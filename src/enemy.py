import pygame
import random
from src.assets import WIDTH, HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/assets/voldy.png")
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))

    def move(self, speed, score_callback):
        self.rect.move_ip(-speed, 0)
        if self.rect.left < 10:
            score_callback(20)
            self.rect.right = WIDTH
            self.rect.center = (WIDTH, random.randint(30, HEIGHT-50))
