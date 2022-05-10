import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # Ctrl+C now works

from pygame.locals import *

from pygame.time import *

from pygame import *

from pygame.locals import *

from math import sqrt

from os import path

from random import *

main_dir = path.split(path.abspath(__file__))[0]



class Game(object):
    
    def __init__(self):
    
        mixer.init()
    
        self.screen = display.set_mode((640, 480))
    
        self.background = image.load(path.join(main_dir, "data", "bg.png"))
    
        self.bar = image.load(path.join(main_dir, "data", "bar.png")).convert_alpha()
    
        self.barrect = self.bar.get_rect()
    
        self.barx, self.bary = 320, 420
    
        self.ball = image.load
