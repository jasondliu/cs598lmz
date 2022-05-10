import gc, weakref

from . import gfx
from . import utils
from . import event
from . import sound
from . import config

from .gfx import Texture, Sprite, Screen
from .event import Event
from .sound import Sound
from .config import Config

class Game:
  def __init__(self, init, update, draw, config = None, name = "Game"):
    self.init = init
    self.update = update
    self.draw = draw
    self.config = config if config != None else Config()
    self.name = name

    self.running = False

    self.fps = 0
    self.delta = 0

    self.screen = None
    self.event = None
    self.sound = None

    self.textures = {}
    self.sprites = {}
    self.sounds = {}

  def __del__(self):
    self.stop()

  def start(self):
    if self.running:
      return

    self.screen = Screen()
    self.event = Event()
    self.sound = Sound()

   
