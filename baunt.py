import pygame

class Baunt(pygame.sprite.Sprite):

    def __init__(self, screen, can):
        """создаем пулю в позиции пушки"""
        super(Baunt, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 1, 10)
        self.color = 0, 0, 0
        self.speed = 5.5
        self.rect.centerx = can.rect.centerx
        self.rect.top = can.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемешение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_baunt(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
