import gc, weakref, shlex
from functools import partial, wraps
from contextlib import contextmanager
from itertools import cycle

from numpy import asarray
from numpy.random import random_integers, random

from . import config
from .sysinit import sysinit
from .utils import *
from .internal_control_flow import *
from .base import *
from .example import *
from . import convolution, coord, datalayer, deprecated, drawing, experiment, \
    gradient, image, init, layer, loss, metrics, noise, optimizer, regularizer, \
    solver, tensor, tools, updater, vis
from .color import rgb
from .color import cmyk
from .color import hsv
from .color import hsl
from .color import hsi
