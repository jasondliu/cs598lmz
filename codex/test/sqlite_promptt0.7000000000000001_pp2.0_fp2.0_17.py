import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:'). The path has to be ':memory:' and not just 'memory'
connection = sqlite3.connect(':memory:')

"""
    This is a class to represent a color.
"""
class RGB:
    """
        The constructor.

        @param red the red value of the color.
        @param green the green value of the color.
        @param blue the blue value of the color.
    """
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    """
        This method returns the red value of a color.

        @return the red value of a color.
    """
    def getRed(self):
        return self.red

    """
        This method returns the green value of a color.

        @return the green value of a color.
    """
    def getGreen(self):
        return self.green

    """
        This method returns the blue value of a color.

        @return the blue value of a color.
    """
