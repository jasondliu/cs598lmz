import weakref

import pygame as pg

from . import prepare
from . import tools


class _StateDict(dict):
    """
    A special dictionary that will be used by states to store
    their attributes.
    """
    def __getattr__(self, attr):
        """
        Return the value of the requested attribute.
        """
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("{} object has no attribute '{}'".format(
                    self.__class__.__name__, attr))

    def __setattr__(self, attr, value):
        """
        Set the value of the requested attribute.
        """
        self[attr] = value

    def __delattr__(self, attr):
        """
        Delete the requested attribute.
        """
        try:
            del self[attr]
        except KeyError:
            raise AttributeError("{} object has no attribute '{}'".format(
                    self.__class__.__name__, attr))

