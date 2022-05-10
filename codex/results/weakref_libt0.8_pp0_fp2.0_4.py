import weakref
import math


from pyglet.gl import *

from pyglet.window import key
from pyglet.window import mouse

from pyglet.window import event
from pyglet.window.event import EventDispatcher

from pyglet.window import page

from pyglet.window.key import KeyStateHandler
from pyglet.window import mouse
from pyglet.window import event
from pyglet.window.event import EventDispatcher
from pyglet.window.event import EventLoop

from pyglet import gl
from pyglet import image
from pyglet import font
from pyglet import clock
from pyglet import app
from pyglet import options as pyglet_options

import util


class Window(EventDispatcher):
    """A window for rendering GL graphics.

    **Overview**

    A Window is a GL rendering context into which graphics are rendered.
    Typically a Window is associated with a Display; it is possible to create
    a "headless" Window which is not associated with any Display.

    By default a Window
