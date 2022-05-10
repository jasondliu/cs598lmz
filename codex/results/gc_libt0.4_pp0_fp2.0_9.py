import gc, weakref

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.graphics.texture import Texture
from kivy.graphics.opengl import glEnable, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND

from kivy.core.window import Window

from kivy.logger import Logger

from kivy.garden.graph import Graph

#from kivy.garden.graph import MeshLinePlot
#from kivy.garden.graph import Graph, MeshStemPlot

import numpy as np

import time

class MyGraph(Graph):
    def __init__(self, **kwargs):
        super(MyGraph, self).__init__(**kwargs)

       
