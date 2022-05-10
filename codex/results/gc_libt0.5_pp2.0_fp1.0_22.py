import gc, weakref

from . import _pygame
from . import _rect
from . import _sdl2
from . import _sdl2_ext
from . import _sdl2_gfx
from . import _sdl2_image
from . import _sdl2_mixer
from . import _sdl2_ttf
from . import _threads
from . import _time
from . import _version
from . import display
from . import draw
from . import event
from . import key
from . import mouse
from . import rect
from . import surface
from . import sysfont
from . import time
from . import version
from . import _freetype_text
from . import _numericsurfarray
from . import _numpysndarray
from . import _pixelcopy
from . import _pixelarray

from . import sndarray
from . import gfxdraw
from . import _camera

from . import locals as _locals

import sys as _sys

__version__ = _version.vernum

_PY3 = _sys.version_info[0]
