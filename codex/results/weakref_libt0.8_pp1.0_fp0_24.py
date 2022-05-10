import weakref
import collections

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, BooleanProperty, \
    OptionProperty, NumericProperty, AliasProperty, DictProperty, \
    ReferenceListProperty, StringProperty, BoundedNumericProperty
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Fbo, ClearColor, ClearBuffer, \
    PushMatrix, PopMatrix, Translate, Scale, Callback, Canvas
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.resources import resource_find
from kivy.animation import Animation
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.utils import platform
from kivy.compat import string_types
from kivy.logger import Logger
from
