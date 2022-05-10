import weakref
import sys

from pymt.graphx.draw import *
from pymt.graphx.instructions import *
from pymt.graphx.gx_matrix import *
from pymt.graphx.gx_color import *
from pymt.graphx.gx_context import *
from pymt.graphx.gx_shader import *

__all__ = [
    'Context', 'Color', 'Matrix', 'Instructions', 'draw', 'set_color',
    'set_matrix', 'set_shader', 'push', 'pop', 'clear', 'reset', 'get',
    'set_context', 'get_context', 'set_default_context', 'get_default_context',
    'set_context_state', 'get_context_state', 'set_default_state',
    'get_default_state', 'set_context_defaults', 'set_default_context_state',
    'set_context_shader', 'get_context_shader', 'set_default_shader',
    '
