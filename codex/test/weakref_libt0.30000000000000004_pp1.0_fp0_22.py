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

