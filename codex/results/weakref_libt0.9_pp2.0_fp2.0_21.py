import weakref
import math
import itertools

import pygame
from pygame.locals import *

from utils import *
import unit

class ActionBase(object):
    def __init__(self, unit_ref):
        self.unit_ref = unit_ref
        self.elapsed_time = 0.0
        self.target = None

    def __repr__(self):
        return self.__class__.__name__

    def update(self, seconds):
        if self.is_finished():
            return None

        self.elapsed_time += seconds
        unit = self.unit_ref()
        if not unit:
            return None
        else:
            return self.run(seconds, unit)

    def run(self, seconds, unit):
        raise NotImplementedError("override me")

    def is_finished(self):
        return False

class MoveAction(ActionBase):
    def __init__(self, unit_ref, unitmap_ref, target):
        super(MoveAction, self).__init__(unit_ref)
