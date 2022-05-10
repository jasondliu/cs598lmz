import gc, weakref

from . import _base
from . import _cairo
from . import _pango

class Context(_cairo.Context):
	__gtype_name__ = 'PangoCairoContext'
	def __new__(cls, font_map=None, *args, **kwargs):
		if font_map is None:
			font_map = _pango.cairo_font_map_get_default()
		return _cairo.Context.__new__(cls, font_map, *args, **kwargs)

class Matrix(_cairo.Matrix):
	__gtype_name__ = 'PangoCairoMatrix'

class Path(_cairo.Path):
	__gtype_name__ = 'PangoCairoPath'

class Pattern(_cairo.Pattern):
	__gtype_name__ = 'PangoCairoPattern'
	def __new__(cls, pattern):
		if isinstance(pattern, _cairo.Pattern):
			return pattern
		return _cairo.Pattern.__new__
