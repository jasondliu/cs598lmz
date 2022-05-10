import weakref
from . import _base
from . import _compat
from . import _util
from . import _vertex
from . import _indexed_vertex
from . import _indexed_triangle_vertex
from . import _indexed_line_vertex
from . import _indexed_point_vertex
from . import _indexed_point_sprite_vertex

#-------------------------------------------------------------------------------

class Renderer(_base.Renderer):
    """
    The interface for a renderer.
    """

    #---------------------------------------------------------------------------

    def __init__(self, window):
        """
        Initialize a renderer.

        :Parameters:
            `window` : `pyglet.window.Window`
                The window to render to.
        """
        super(Renderer, self).__init__()
        self.window = window
        self._vbo = None

    #---------------------------------------------------------------------------

    def on_resize(self, width, height):
        """
        Called when the window is resized.
        """
        pass

    #---------------------------------------------------------------------------

    def on_
