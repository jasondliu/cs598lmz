import gc, weakref

from . import _core
from . import _util
from . import _data
from . import _shaders
from . import _view
from . import _scene
from . import _collections
from . import _widgets
from . import _animation
from . import _traits
from . import _app
from . import _testing


__all__ = ['enable_depth_peeling', 'get_depth_peeling_stacks', 'get_depth_peeling_layers',
           'set_depth_peeling_layers', 'set_depth_peeling_stacks', 'set_depth_peeling_threshold',
           'get_depth_peeling_threshold', 'get_depth_peeling_max_layers',
           'set_depth_peeling_max_layers', 'set_depth_peeling_transparency_sorting',
           'get_depth_peeling_transparency_sorting', 'set_depth_peeling_transparency_sorting_threshold',
           'get_depth_peeling_transparency_sorting_threshold
