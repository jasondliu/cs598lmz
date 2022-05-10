import weakref

import pygame as pg
from pygame.sprite import Sprite

import prepare, tools


class Tile(Sprite):
    """Tile sprite.  Has two images, one for occupied and one for empty."""
    def __init__(self, topleft, game):
        super(Tile, self).__init__()
        self.game = weakref.ref(game)
        self.interior = pg.Surface(prepare.CELL_SIZE).convert()
        self.interior.fill((200, 200, 200))
        self.surface = pg.Surface(prepare.CELL_SIZE).convert()
        self.rect = self.surface.get_rect(topleft=topleft)
        self.contents = None

    def update(self, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos):
            self.surface.fill((100, 100, 100))
            if mouse_click:
                self.game().select_tile(self)
