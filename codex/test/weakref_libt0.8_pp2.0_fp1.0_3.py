import weakref

import pygame

import core
from core import Config, Game, State
import display
import level
import util
import sound


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.group = self.game.player_group

        self.moved = 0 # The number of moves the player has made since they moved
        self.steps = 0 # The number of steps the player has made this turn

        self.no_message = False
        self.rested = False

        self.health = Config.max_health
        self.max_health = Config.max_health

        self.max_mana = Config.max_mana
        self.mana = self.max_mana

        self.notify_regeneration = False

        self.strength = Config.strength
        self.armor = Config.armor
        self.accuracy = Config.accuracy

