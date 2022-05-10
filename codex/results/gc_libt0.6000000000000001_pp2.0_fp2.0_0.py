import gc, weakref
import math

#from pydispatch import dispatcher
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty, ListProperty, BooleanProperty, StringProperty, DictProperty
from kivy.vector import Vector
from kivy.animation import Animation
from kivy.lang import Builder
Builder.load_string('''
#:import math math
<Ball>:
    size: 30, 30
    canvas:
        Color:
            hsv: self.h, 1, 1
        Ellipse:
            pos: self.pos
            size: self.size
''')

class Ball(Widget):
    angle = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    h = NumericProperty(0)

    def __
