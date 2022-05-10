import weakref

from .. import _base
from .. import core
from .. import events
from .. import gloo
from .. import gl
from .. import config
from ..util import logger
from ..util import lru_cache
from ..util.event import EmitterGroup
from ..util.ptime import time
from . import _base_sdl2 as sdl2

# -------------------------------------------------------------------- Init ---

_canvas = None

_canvas_classes = {
    'sdl2': 'vispy.app.backends.sdl2._canvas.CanvasBackend'
}


def _get_canvas_class(name):
    """Get the canvas class for a given backend name."""
    if name in _canvas_classes:
        class_name = _canvas_classes[name]
