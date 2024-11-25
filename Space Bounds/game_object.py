import pygame
import random
from game_setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")  
        self.image = pygame.transform.scale(self.image, (60, 80))  
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 8
        self.lives = 0

    def take_damage(self):
        self.lives -= 1
        if self.lives <= 0:
            return True  
        return False
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT  ] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed  
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed  
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        enemy_images = ["enemy3.png"]
        self.image = pygame.image.load(random.choice(enemy_images))  
        self.image = pygame.transform.scale(self.image, (80, 100))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.hp = 1
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.kill()

class BossEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("boss1.png")
        self.image = pygame.transform.scale(self.original_image, (448.5, 277))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 100)  
        self.hp = 50 * 1
        self.flash = False  
        self.speed_x = 3  
        self.speed_y = 2  
     
    def take_damage(self, amount):
        self.hp -= amount
        self.flash = True  
        if self.hp <= 0:
            self.kill()

    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= 1550:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= 970:
            self.speed_y *= -1

        if self.flash:
            self.image.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)  
            self.flash = False
        else:
            self.image = pygame.transform.scale(self.original_image, (448.5, 277))  

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 6))
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -20
        self.damage = 1
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()