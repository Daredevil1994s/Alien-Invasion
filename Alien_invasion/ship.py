import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его нач. позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('D:\Alien_game\images\ship.bmp')
        # Изменение размера изображения корабля
        self.image = pygame.transform.scale(self.image, (50, 50))  # Задайте желаемый размер (ширина, высота)
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию коробля с учетом флагов"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        # Обновляется атрибут х, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Размещает корабль в центре нижней стороны'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)