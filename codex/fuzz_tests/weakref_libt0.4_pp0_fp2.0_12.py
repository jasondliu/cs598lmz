import weakref

from pyglet.gl import *
from pyglet.graphics import Batch
from pyglet.window import key

from cocos.director import director
from cocos.actions import *
from cocos.layer import *
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.menu import *

from src.map import Map
from src.player import Player
from src.enemy import Enemy
from src.collision_manager import CollisionManager
from src.camera import Camera
from src.game_controller import GameController
from src.game_over_scene import GameOverScene
from src.game_scene import GameScene
from src.menu_scene import MenuScene
from src.constants import *

class Game(Layer):

    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()

        self.map = Map(MAP_WIDTH, MAP_HEIGHT)
        self.player = Player(self.map)
        self.enemies =
