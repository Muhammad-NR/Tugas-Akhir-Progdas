import pygame
from game_setting import *

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50, 200, 50)
        self.exit_button = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 20, 200, 50)
        if self.play_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, DARK_CYAN, self.play_button, 0, border_radius=20)
    
    def draw_score(self, score):
        score_text = TINY_TEXT.render(f'Score: {score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
    
    def draw_pause(self):
        pause_text = LARGE_TEXT.render('PAUSED', True, WHITE)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        
        resume_text = TINY_TEXT.render('Press P to Resume', True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75))
        
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
    
    def draw_game_over(self, score):
        game_over_text = LARGE_TEXT.render('GAME OVER', True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        restart_text = TINY_TEXT.render('Press R to Restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 75))
        
        score_text = SMALL_TEXT.render(f'Score : {score}', True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 225))
        
        padding = 10  
        box_width = score_rect.width + padding * 2
        box_height = score_rect.height + padding * 2
        box_rect = pygame.Rect(score_rect.centerx - box_width / 2, score_rect.centery - box_height / 2, box_width, box_height)
        
        border_width = 3  
        corner_radius = 20  
        pygame.draw.rect(self.screen, WHITE, box_rect, border_width, border_radius=corner_radius)
        self.screen.blit(score_text, score_rect)

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(restart_text, restart_rect)
        
    
    def draw_home_screen(self, background, logo_image):
        self.screen.blit(background, (0, 0))
        logo_rect = logo_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
        self.screen.blit(logo_image, logo_rect)
    
        title_text = LARGE_TEXT.render('Space Bounds', True, DARK_CYAN)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + 50))

        play_text = TINY_TEXT.render('Play', True, BLACK)
        exit_text = TINY_TEXT.render('Exit', True, BLACK)

        pygame.draw.rect(self.screen, WHITE, self.play_button, 0, border_radius=20)
        pygame.draw.rect(self.screen, WHITE, self.exit_button, 0, border_radius=20)
        
        self.screen.blit(title_text, title_rect)
        self.screen.blit(play_text, play_text.get_rect(center=self.play_button.center))
        self.screen.blit(exit_text, exit_text.get_rect(center=self.exit_button.center))
    
    def draw_you_won(self, score):
        you_won_text = LARGE_TEXT.render('YOU WON!', True, GREEN)
        you_won_rect = you_won_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        
        score_text = SMALL_TEXT.render(f'Final Score: {score}', True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
        padding = 10  
        box_width = score_rect.width + padding * 2
        box_height = score_rect.height + padding * 2
        box_rect = pygame.Rect(score_rect.centerx - box_width / 2, score_rect.centery - box_height / 2, box_width, box_height)
        
        border_width = 3  
        corner_radius = 20  
        pygame.draw.rect(self.screen, WHITE, box_rect, border_width, border_radius=corner_radius)
        self.screen.blit(score_text, score_rect)
        
        restart_text = TINY_TEXT.render('Press R to Restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))
        
        exit_text = TINY_TEXT.render('Press Esc to Exit', True, WHITE)
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 250))
        
        self.screen.blit(you_won_text, you_won_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(exit_text, exit_rect)
        
    def exit_game(self):
        exit_game_text = TINY_TEXT.render('Press Esc to Exit', True, WHITE)        
        text_rect = exit_game_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 125))
        self.screen.blit(exit_game_text, text_rect)
        