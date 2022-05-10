import weakref

from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Line, Rectangle
from kivy.graphics.instructions import InstructionGroup

from . import utils
from . import config

class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)

        self.show_axes = True
        self.show_grid = True
        self.show_labels = True

        self.font_size = 10
        self.grid_size = 10
        self.tick_size = 10
        self.tick_label_offset = 5

        self.t = 0

        self.graphs = []

        self.bind(size=self.update_graph)
        self.bind(
