import gc, weakref
import os, sys
import time
import re
import traceback

from . import _cairo, _cairo_ft, _cairo_xlib, _cairo_xlib_xrender
from . import _cairo_ps, _cairo_pdf, _cairo_svg

from . import _cairo_win32

from . import _cairo_win32_surface
from . import _cairo_win32_font
from . import _cairo_win32_printing

from . import _cairo_win32_dynamic

from . import _cairo_win32_gdi

from . import _cairo_win32_scaled_font

from . import _cairo_win32_font_face

from . import _cairo_win32_ft

from . import _cairo_win32_surface_fallback

from . import _cairo_win32_surface_fallback_compositor

from . import _cairo_win32_surface_fallback_compositor_solid

from . import _cairo
