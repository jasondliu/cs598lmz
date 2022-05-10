import gc, weakref

from IPython.core.getipython import get_ipython
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import (
    argument, magic_arguments, parse_argstring
)

from IPython.lib.lexers import IPythonLexer, IPyLexer
from pygments.formatters import TerminalTrueColorFormatter

from IPython.utils.py3compat import cast_unicode
from IPython.core.display import HTML

import IPython.terminal.pt_inputhooks as pt_inputhooks
from IPython.terminal.pt_inputhooks.pyqt5  import QtInputHook
from IPython.terminal.pt_inputhooks.pyglet import PygletInputHook
from IPython.terminal.pt_inputhooks.pygame import PyGameInputHook
from IPython.terminal.pt_inputhooks.glfw   import GlfwInputHook
from IPython.terminal.pt_in
