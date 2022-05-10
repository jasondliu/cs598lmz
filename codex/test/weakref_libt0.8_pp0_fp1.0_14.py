import weakref
import time
import copy

from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Color, Rectangle
from kivy.graphics.opengl_utils import glColor4f
from kivy.uix.stencilview import StencilView
from kivy.app import App
from kivy.logger import Logger
from kivy.base import stopTouchApp, EventLoop, ExceptionManager
from kivy.compat import string_types
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.audio import SoundLoader
from kivy.graphics.opengl import glBlendFunc
from kivy.properties import ListProperty, BooleanProperty, StringProperty
