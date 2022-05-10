import weakref

from pyglet.gl import *
from pyglet.window import key

from cocos.director import director
from cocos.layer import Layer
from cocos.menu import *
from cocos.sprite import Sprite
from cocos.scenes.transitions import *

from config import *
from constants import *
from game import *
from game_scene import *

def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Main Menu')

        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['color'] = (204,164,164,255)
        self.font_title['font_size'] = 72

        self.font_item['color'] = (32,16,32,255)
        self.font_item['font_size'] = 32
