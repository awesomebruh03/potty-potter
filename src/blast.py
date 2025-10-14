import pygame
from src.assets import blast_images

class Blast(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = blast_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def move(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(blast_images):
                self.kill()
            else:
                self.image = blast_images[self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
