import weakref

from .. import _base
from .. import core
from .. import events
from .. import graphics
from .. import input
from .. import window


class _GLFWWindow(_base.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._glfw_window = None

    def _create_window(self, width, height, title, resizable, style, vsync):
        if self._glfw_window is not None:
            raise RuntimeError("Window already created")

        # Create the window
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window
