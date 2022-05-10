import ctypes
ctypes.windll.user32.SetProcessDPIAware()

#Compatibility Workaround
from src.ecs.components import *
from src.ecs.systems import *
from src.engine.engine import Engine
from src.ecs.entity import Entity
from src.ecs.utils import Vec2d
from src.data.dataparser import parseData
from src.engine.debugging import Debugging
from src.mapgen.map import Map

from src.engine.eventhandler import EventHandler
from src.ecs.components.components import *
from src.ecs.components.components import isMovementComponent


from src.componentsCommon import *
from src import constants

from functools import partial
import time

from src.other_modules.colored_traceback.colored_traceback import *
from src.other_modules.pgu import gui
from src.rendering.globals import *

from src.mapgen.map import Map



state = ""

#def create_engine():
#    global STATE
#    #Sets the
