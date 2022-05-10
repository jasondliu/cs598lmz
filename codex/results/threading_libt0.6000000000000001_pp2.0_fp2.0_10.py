import threading
threading.stack_size(2**27)
import sys
import pyglet
from pyglet.window import key
from pyglet.gl import *
from pyglet.window import mouse
import time
import os
import random
import pickle
import math
import resource
import glob
import cocos
import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.actions as ac

from OpenGL.GL import *
import numpy as np

import pyglet.resource
pyglet.resource.path.append('data/')
pyglet.resource.reindex()

import render
import world_objects
import world_map
import game_state
import world_generator
import map_editor
import game_constants
import ui
import menu
import game
import config
import mapper
import menu_item
import sound
import shader
import ai

# This is a hack to get around the fact that pyglet doesn't have
# a window.set_icon command
os.environ['SDL_VIDEO_CENTER
