import weakref
from .tick import (tickManager, ticks, ticksList,
                   tickAssignPixel, tickAssignSpot, tickAssignRegion,
                   tickAssignLabel, tickAssignSeqLevel)
from . import zTetris

# 
class zTetrisTable(object):
    """
    This is a class that manages the tetris regions and pixels.
    """
    
    def __init__(self, width, height):
        """
        Constructor.
        
        :param width: (int) width
        :param height: (int) height
        """
        self.__width = width
        self.__height = height
        self.__tetrisList = []
        self.__tetrisRowPos = 0
        self.__tetrisColPos = 0
        self.__tetrisLevel = 0
        self.__tetrisPixel = {}
        self.__tetrisRegion = {}

        self.__tetrisPixelMap = []
        for irow in range(height):
            row = []
