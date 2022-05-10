import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from vizdoom import *
import itertools as it
import pickle

from random import sample, randint, random
from time import time, sleep
import numpy as np

import keras
from keras.utils.np_utils import to_categorical

from vizdoom import *

print("Initializing doom...")
# Create DoomGame instance. It will run the game and communicate with you.
game = DoomGame()

# Now it's time for configuration!
# load_config could be used to load configuration instead of doing it here with code.
# If load_config is used in-code configuration will also work - most recent changes will add to previous ones.
# game.load_config("../../scenarios/basic.cfg")
# game.load_config("../../scenarios/simpler_basic.cfg")
game.load_config("./deadly_corridor.cfg")
#game.load_config("./defend_the_center.cfg")
game.set_render_hud
