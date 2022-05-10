import gc, weakref

from . import _cairo, Image
from . import _cairo_ft, _cairo_ft_font
from . import _cairo_ps, _cairo_ps_surface
from . import _cairo_pdf, _cairo_pdf_surface
from . import _cairo_svg, _cairo_svg_surface
from . import _cairo_win32, _cairo_win32_surface
from . import _cairo_quartz, _cairo_quartz_surface
from . import _cairo_xlib, _cairo_xlib_surface
from . import _cairo_xcb, _cairo_xcb_surface
from . import _cairo_drm, _cairo_drm_surface
_cairo_gl = _cairo_xcb = _cairo_drm = None
_cairo_gl_surface = _cairo_xcb_surface = _cairo_drm_surface = None

from . import _cairo_gl, _cairo_gl_surface
from . import _cairo_xcb, _cairo_x
