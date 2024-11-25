import pygame
import sys
import random
from game_object import Player, Enemy, Bullet, BossEnemy
from gui import GUI
from game_setting import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Bounds")
        self.clock = pygame.time.Clock()
        self.gui = GUI(self.screen)
        
        self.background = pygame.image.load("bg1.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.logo_image = pygame.image.load("boss1.png")
        self.logo_image = pygame.transform.scale(self.logo_image, (897, 554))
        
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.score = 0
        self.game_over = False 
        self.home_screen = True
        self.boss_spawned = False
        self.pause = False
        self.you_won = False
        self.enemy_killed = 0  
            
    def spawn_enemy(self):
        if not self.boss_spawned and self.enemy_killed >= 10:  
            boss = BossEnemy()
            self.all_sprites.add(boss)
            self.enemies.add(boss)
            self.boss_spawned = True
        elif not self.boss_spawned:  
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if self.game_over or self.you_won:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:  
                        pygame.quit()
                        sys.exit()
                continue  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.pause:
                    bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
                elif event.key == pygame.K_p and not self.home_screen:
                    self.pause = not self.pause

            if event.type == pygame.MOUSEBUTTONDOWN and self.home_screen:
                mouse_pos = pygame.mouse.get_pos()
                if self.gui.play_button.collidepoint(mouse_pos):
                    self.home_screen = False
                elif self.gui.exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        return True
    
    def update(self):
       if not self.home_screen and not self.game_over and not self.pause:
            self.all_sprites.update()
            
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for hit in hits:
                if isinstance(hit, BossEnemy):
                    hit.take_damage(1)  
                    if hit.hp <= 0:
                        self.boss_spawned = False  
                        self.score += 20000
                        self.you_won = True
                else:    
                    hit.kill()
                    self.enemy_killed += 1  
                    self.score += 500
                    self.spawn_enemy()
            
            if pygame.sprite.spritecollide(self.player, self.enemies, False):
                if self.player.take_damage():
                    self.game_over = True
            
            if self.you_won or self.game_over:
                self.bullets.empty()

    def draw(self):
        if self.home_screen:
            self.gui.draw_home_screen(self.background, self.logo_image)
        elif self.you_won:  
            self.screen.blit(self.background, (0, 0))
            self.gui.draw_you_won(self.score)
        elif self.game_over:
            self.screen.blit(self.background, (0, 0))
            self.gui.draw_game_over(self.score)
            self.gui.exit_game()
        
        elif self.pause:  
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.gui.draw_pause()
        else:
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.gui.draw_score(self.score)
            
        pygame.display.flip()   
    
    def reset_game(self):
        self.all_sprites.empty()  
        self.enemies.empty()    
        self.bullets.empty()      
        self.player = Player()
        self.all_sprites.add(self.player)
        self.score = 0
        self.enemy_killed = 0 
        self.game_over = False
        self.you_won = False
        self.boss_spawned = False

        for _ in range(15):  
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
        
        self.spawn_enemy()
     
    def run(self):
        running = True
        for _ in range(15):
            self.spawn_enemy()
            
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()