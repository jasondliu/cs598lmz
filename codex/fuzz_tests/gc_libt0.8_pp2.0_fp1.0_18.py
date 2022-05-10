import gc, weakref
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.properties import ObjectProperty,StringProperty,NumericProperty,BooleanProperty
from kivy.graphics import Color, Mesh
from kivy.graphics.opengl import glEnable, glDisable
from kivy.graphics.texture import Texture
from kivy.graphics.transformation import Matrix
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.vector import Vector
import math
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

from kivy.uix.floatlayout import FloatLayout

from kivy.clock import Clock
from
