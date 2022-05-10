import types
types.ModuleType.__dict__.update(dict(
    __file__ = __file__,
    __loader__ = __loader__,
    __path__ = __path__,
    __name__ = __name__,
    __package__ = __package__,
    __doc__ = __doc__,
    __all__ = __all__,
    __version__ = __version__,
    ))

# Import the module
from . import _libtcodpy as libtcod

# Import the public API
from . import _public_api as public_api

# Import the public API
from . import _public_types as public_types

# Initialize the module
libtcod.TCOD_console_set_custom_font(
    os.path.join(os.path.dirname(__file__), "terminal.png"),
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD,
    0, 0
    )
libtcod.TCOD_console_init_root(
    80,
