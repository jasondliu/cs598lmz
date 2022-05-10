import gc, weakref
from collections import OrderedDict, defaultdict

from kivy.metrics import dp
from kivy.uix.effectwidget import EffectWidget, PixelEffect
from kivy.graphics import Color, Line, InstructionGroup, Quad
from kivy.graphics.instructions import RenderContext
from kivy.graphics.transformation import Matrix
from kivy.animation import Animation
from kivy.logger import Logger
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.compat import string_types
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kiv
