import pygame
from src.assets import WHITE, YELLOW, font_name, WIDTH, HEIGHT

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def load_high_score():
    try:
        with open('high_score.txt', 'r') as file:
            high_score_str = file.read().strip()
            if high_score_str.isdigit():
                return int(high_score_str)
            else:
                return 0
    except FileNotFoundError:
        return 0
    except Exception as e:
        print('loading error', str(e))
        return 0

def save_high_score(score):
    try:
        with open('high_score.txt', 'w') as file:
            file.write(str(score))
    except Exception as e:
        print('saving error', str(e))
