import pygame

WIDTH = 900
HEIGHT = 600
WHITE = (255, 255, 255)
YELLOW = (255, 191, 0)
font_name = "src/assets/HARRYP__.TTF"

background = pygame.image.load("src/assets/starfield.png")
background_rect = background.get_rect()
live_ = pygame.image.load("src/assets/bolt_gold.png")
live_bar = pygame.transform.scale(live_, (30, 30))
blast_images = [pygame.image.load(f"src/assets/b{i}.png") for i in range(1, 9)]
