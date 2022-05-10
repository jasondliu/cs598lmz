import weakref
import time
import random
import logging

import numpy as np

from . import gl, glu, glut
from . import util
from . import camera
from . import model
from . import texture
from . import shader
from . import viewport
from . import scene
from . import material
from . import light
from . import widget
from . import shader
from . import fbo
from . import font

log = logging.getLogger(__name__)


class BaseContext(object):
    """
    Base class for contexts.
    """
    def __init__(self):
        self._viewports = []
        self.viewports = []
        self._viewport_dict = {}
        self._viewport_name_dict = {}
        self._viewport_order = []
        self._viewport_order_dict = {}
        self._viewport_order_names = []
        self._viewport_order_names_dict = {}
        self._viewport_order_names_dict_inv = {}
        self._viewport_order_name_dict = {}

