import weakref

import pygame as pg

from .. import prepare
from ..components import animation, body
from ..components.labels import Label
from ..components.labels import Blinker
from ..components.ui import Button
from ..components.ui import ScreenBackground
from ..components.ui import ScreenFade
from ..components.ui import TextBox
from ..components.ui import TransitionBox
from ..components.ui import Window


class Player(Animation):
    def __init__(self, player_num, pos, name="", *groups):
        super(Player, self).__init__(prepare.GFX["p{}".format(player_num)],
                                        pos, *groups)
        self.frame_index = 0
        self.last_update = 0
        self.current_time = 0
        self.frame_rate = 100
        self.loop = True
        self.load_frames()
        self.rect.left, self.rect.bottom = pos
        self.state = None
        self.timer = 0
        self.speed = 0

