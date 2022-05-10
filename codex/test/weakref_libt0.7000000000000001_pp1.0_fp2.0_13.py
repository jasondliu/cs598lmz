import weakref

from numpy import random as nprandom

from . import util
from . import config
from . import datatypes
from . import userinput
from . import primitives
from . import level
from . import monsters
from . import items

from . import actors

from . import debug


# ##############################################
# Support functions
# ##############################################

def gen_random_floor(dimensions, depth, map_type=None):
    """Generate a random floor, with a staircase placed on it."""
    if map_type == None:
        map_type = level.FloorMap
    m = map_type(dimensions, depth)
    m.create_floor()

    return m

def gen_random_corridor_floor(dimensions, depth, num_corridors, map_type=None):
    """Generate a random corridor floor."""
    if map_type == None:
        map_type = level.FloorMap
    m = map_type(dimensions, depth)
    m.create_floor()
