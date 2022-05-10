import types
types.ClassType = type

import unittest

import pygame
from pygame.compat import as_unicode, unicode_

import pygame.locals as locals

from pygame.tests.test_utils import arrange_rects, unittest, \
    geterror

PY3 = geterror() == 'surfarray module not available'

if not PY3:
    import pygame.surfarray as surfarray


def surf_to_array(surf):
    """Convert a surface to a numpy array and return it."""
    return surfarray.array2d(surf)


def array_to_surf(arr):
    """Convert a numpy array to a surface and return it."""
    return surfarray.make_surface(arr)


class SurfaceArrayModuleTest(unittest.TestCase):
    """Generic test class for surfarray module."""

    def setUp(self):
        """Setup the test environment."""
        pygame.display.init()

