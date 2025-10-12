
#Imports
import pygame, sys
from pygame.locals import *
import random, time
import pygame.mixer

pygame.init()
pygame.mixer.init()
FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
YELLOW = (255, 191, 0)

WIDTH = 900
HEIGHT = 600
SPEED = 10
MAX_SPEED = 15


background = pygame.image.load("starfield.png")
background_rect = background.get_rect()
font_name = "HARRYP__.TTF"

DISPLAYSURF = pygame.display.set_mode((900,600))
pygame.display.set_caption("The Harry Potter Game")

pygame.mixer.music.load("game_bg.wav")
pygame.mixer.music.play (-1)

start_page = pygame.Surface((WIDTH, HEIGHT))
start_page.blit(background, (0, 0))
start_font = pygame.font.Font(font_name, 30)
start_text = start_font.render("Press any key to start", True,YELLOW)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 2, HEIGHT // 1.2)
start_page.blit(start_text, start_text_rect)


start_font = pygame.font.Font(font_name, 60)
start_text = start_font.render("The", True, YELLOW)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 7.9, HEIGHT // 7.1)
start_page.blit(start_text, start_text_rect)

start_font = pygame.font.Font(font_name, 70)
start_text = start_font.render("Game", True, YELLOW)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 1.17, HEIGHT // 1.9)
start_page.blit(start_text, start_text_rect)

start_font = pygame.font.Font(font_name, 30)
start_text = start_font.render("Use the arrow keys to move", True, YELLOW)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 2, HEIGHT // 1.3)
start_page.blit(start_text, start_text_rect)

start_font = pygame.font.Font(font_name, 15)
start_text = start_font.render("All the characters belong to J K Rowling", True, YELLOW)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 2, HEIGHT // 1.05)
start_page.blit(start_text, start_text_rect)

start_image = pygame.image.load("potter.png")
start_page.blit(start_image,(WIDTH//2.5, HEIGHT//2))
start_image = pygame.image.load("start.png")
start_page.blit(start_image,(WIDTH//14, HEIGHT//22))

game_state = "start_page"

#score

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

    
#lives

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
live_ = pygame.image.load("bolt_gold.png")
live_bar = pygame.transform.scale(live_,(30,30))

#baaler potter
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("potter.png")
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
               self.rect.move_ip(0, -SPEED)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[K_DOWN]:
               self.rect.move_ip(0,SPEED)    
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-SPEED, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(SPEED, 0)
        
    
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
              self.hidden = False
              self.rect.center = (100,160)


#voldemort er gushti chudi
class Enemy(pygame.sprite.Sprite):
      def __init__(self):

        super().__init__() 
        self.image = pygame.image.load("voldy.png")
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.center = (900, random.randint(30,550))

      def move(self):
        global SCORE
        self.rect.move_ip(-SPEED,0)
        if (self.rect.left < 10):
            SCORE += 20
            self.rect.right = 900
            self.rect.center = (900, random.randint(30,550))

      def get_random_y(self):
          while True: 
              y=random.randint(30,550)
              if not pygame.sprite.spritecollideand(self,coins,pygame.sprite.collide_rect):
                  return y
            
#kha kha khaaaaaaa                
class Coin1(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.center=(900, random.randint(30,550))

      def move(self):
        global SCORE
        self.rect.move_ip(-1.25*SPEED,0)
        if (self.rect.left < 10):
            self.rect.right = 900
            self.rect.center = (900, random.randint(30,550))

      def get_random_y(self):
        while True:
            y=random.randint(30,550)
            if not pygame.sprite.spritecollideand(self,sep1,pygame.sprite.collide_rect):
                return y
     
#kha kha khaaa222222
class Coin2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.radius = 30
        self.rect.center=(900, random.randint(30,550))

      def move(self):
        global SCORE
        self.rect.move_ip(-1.25*SPEED,0)
        if (self.rect.left < 10):
            self.rect.right = 900
            self.rect.center = (900, random.randint(30,550))

      def get_random_y(self):
        while True:
            y=random.randint(30,550)
            if not pygame.sprite.spritecollideand(self,sep2,pygame.sprite.collide_rect):
                return y
point_sound = pygame.mixer.Sound('point.wav')    

blast_images = [pygame.image.load("b1.png"), pygame.image.load("b2.png"), pygame.image.load("b3.png"),pygame.image.load("b4.png"), pygame.image.load("b5.png"), pygame.image.load("b6.png"),pygame.image.load("b7.png"), pygame.image.load("b8.png")]
blast_index = 0
blast_sound = pygame.mixer.Sound('blast.wav')
#avada kedavra green hoy, green blast khoj magi
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


def load_high_score():
    try:
        with open ('high_score.txt', "r" ) as file:
            high_score_str = file.read().strip()
            if high_score_str.isdigit():
                return int(high_score_str)
            else:
                return 0
    except FileNotFoundError:
        return 0
    except Exception as e :
        print ('loading error', str(e))
        return 0
    
def save_high_score(score):
    try:

      with open('high_score.txt','w') as file:
        file.write(str(SCORE))
    except Exception as e:
        print ('saving error', str(e))


SCORE = 0
HIGHEST_SCORE = load_high_score()

if SCORE > HIGHEST_SCORE:
     HIGHEST_SCORE = SCORE
     save_high_score(HIGHEST_SCORE)
    


def game_over_screen(score):
    game_over_surf = pygame.Surface((WIDTH, HEIGHT))
    game_over_surf.blit(background, (0, 0))
    font = pygame.font.Font(font_name, 150)
    game_over_text = font.render ("GAME OVER",True, YELLOW)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (WIDTH //2, HEIGHT //2 - 60)
    game_over_surf.blit(game_over_text, game_over_rect)

    font = pygame.font.Font(font_name, 60)
    score_text = font.render(f"Your Score: {SCORE}", True, YELLOW)
    score_rect = score_text.get_rect()
    score_rect.center = (WIDTH // 2, HEIGHT // 2+40)
    game_over_surf.blit(score_text,score_rect)

    HIGHEST_SCORE = load_high_score()
    if SCORE > HIGHEST_SCORE:
     HIGHEST_SCORE = SCORE
     save_high_score(HIGHEST_SCORE)
    
    highest_score_text = font.render(f"Highest Score: {HIGHEST_SCORE}", True, YELLOW)
    highest_score_rect = highest_score_text.get_rect()
    highest_score_rect.center = (WIDTH // 2, HEIGHT // 2+100)
    game_over_surf.blit(highest_score_text,highest_score_rect)

    DISPLAYSURF.blit(game_over_surf,(0,0))

             
game_over_screen(SCORE)

#Sprites bhalo na, only cocacola is real        
P1 = Player()
E1 = Enemy()
C1 = Coin1()
C2 = Coin2()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins1 = pygame.sprite.Group()
coins1.add(C1)
coins2 = pygame.sprite.Group()
coins2.add(C2)
sep1 = pygame.sprite.Group()
sep1.add (E1)
sep1.add (C2)

sep2 = pygame.sprite.Group()
sep2.add (E1)
sep2.add (C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)


if P1.lives == 0:
    for enemy in enemies:
        enemy.kill()

#new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
  
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if game_state == "start_page":
            DISPLAYSURF.blit(start_page, (0, 0))
            
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
            DISPLAYSURF.blit(background, (0,0))
            #DISPLAYSURF.blit(background, background_rect)
            all_sprites.draw(DISPLAYSURF)
            draw_text(DISPLAYSURF, str(SCORE), 30, 30, 10)
            draw_lives(DISPLAYSURF, 800, 10, P1.lives , live_bar)
            all_sprites.update()
            
               
            hits2 = pygame.sprite.spritecollide(P1, enemies, True, pygame.sprite.collide_circle)
            for hit in hits2:
                P1.lives -= 1
                blast = Blast(hit.rect.centerx, hit.rect.centery)
                blast_sound.play()
                all_sprites.add(blast)
                E1 = Enemy()
                enemies.add(E1)
                all_sprites.add(E1)
              
            
            #scoreeee mamaaaah
            hits1 = pygame.sprite.spritecollide(P1, coins1, False, pygame.sprite.collide_circle)
            for hit in hits1:
                if hit==C1:
                 SCORE +=50
                 point_sound.play()
                 hit.kill()
                 C1=Coin1()
                 coins1.add(C1)
                 all_sprites.add(C1)

            hits2 = pygame.sprite.spritecollide(P1, coins2, False, pygame.sprite.collide_circle)
            for hit in hits2:
                if hit==C2:
                 SCORE +=50
                 point_sound.play()
                 hit.kill()
                 C2=Coin2()
                 coins2.add(C2)
                 all_sprites.add(C2)
                
            

            if P1.lives == 0:
               game_state = "game_over"
    elif game_state == "game_over":
            for enemy in enemies:
                enemy.kill()
       
            game_over_screen(SCORE)
            pygame.display.update()
            time.sleep(6)
            pygame.quit()
            sys.exit()

        
    pygame.display.update()
    FramePerSec.tick(FPS)
