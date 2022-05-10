import gc, weakref

from . import _cocos2d

from . import director
from . import action
from . import layer
from . import scene
from . import sprite
from . import label
from . import menu
from . import transition
from . import grid
from . import tilemap
from . import draw
from . import event
from . import touch
from . import key
from . import accelerometer
from . import scheduler
from . import texture
from . import shader
from . import text
from . import gl
from . import audio
from . import config
from . import sprite_frame
from . import animation
from . import particle_system
from . import physics
from . import math
from . import geometry
from . import draw_primitives
from . import layers
from . import actions
from . import effects
from . import widgets
from . import components
from . import ccs
from . import sprite3d
from . import navmesh
from . import js

#
# Cocos2d-x compatibility
#

class _EventListener(object):
    def __init__(self, listener, event_type,
