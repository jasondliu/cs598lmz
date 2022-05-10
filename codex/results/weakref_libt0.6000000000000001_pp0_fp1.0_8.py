import weakref
import logging
import math

class Object(object):
    """
    Object class. All game objects should inherit from this.
    """

    def __init__(self, x, y, width, height, world, name, group=None, type=None):
        """
        Initialization.
        """

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._world = world
        self._name = name
        self._group = group
        self._type = type

        self._dx = 0
        self._dy = 0

        # whether the object is stationary or not
        self._stationary = False

        # whether the object is visible or not
        self._visible = True

        # list of objects that this object collides with
        self._collide_list = []

        self._world.add_object(self)

    def __repr__(self):
        """
        Representation.
        """

        return "Object(x=%s, y=%s, width=%s, height=
