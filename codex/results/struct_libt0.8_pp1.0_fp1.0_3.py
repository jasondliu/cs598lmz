import _struct
from _struct import unpack, pack
import time
import aggdraw
import PIL.Image, PIL.ImageDraw, PIL.ImageFilter
import operator
import numpy
import math
import copy
import numpy
from numpy import array,uint8

from numpy.linalg import eigvalsh


## DEFINITIONS FOR TILES

class Tile(object):
    """ This is a tile class. Each tile represents one square unit of territory
    that can be controlled by one country. A tile has a (x,y) coordinate, a 
    continent, an owner, and an army size. A tile can also be occupied, 
    which means that the tile is currently a part of a game and is not 
    available for other games. A tile can also be impassable, which will 
    prevent any army from crossing it.
    """

    def __init__(self,coords,continent,owner=None,armySize=None):
        super(Tile,self).__init__()
        self.coords = coords # (x,y)
       
