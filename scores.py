import pygame.font
from can import Can
from pygame.sprite import Group

class Scores():
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        """инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 203, 14)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_cans()

    def image_score(self):
        """преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (255, 255, 255))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (255, 255, 255))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_cans(self):
        """колличество жизней"""
        self.cans = Group()
        for can_number in range(self.stats.cans_left):
            can = Can(self.screen)
            can.rect.x = 15 + can_number * can.rect.width
            can.rect.y = 20
            self.cans.add(can)


    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.cans.draw(self.screen)