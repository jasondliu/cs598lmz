import weakref

import pygame as pg


class Ship(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image  # Изображение корабля
        self.rect = self.image.get_rect().move(x, y)  # Координаты и размеры корабля
        self.mask = pg.mask.from_surface(self.image)  # Маска корабля

    def move(self):
        """Передвигает корабль в зависимости от клавиш пользователя"""
        key = pg.key.get_pressed()  # Полу
