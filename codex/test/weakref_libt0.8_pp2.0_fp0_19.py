import weakref, re, gc

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty)
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.vector import Vector
from kivy.geometry import Triangle
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rotate, PushMatrix, PopMatrix
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from lista import Lista
from pila import Pila
from cola import Cola
from arbol import ArbolBinario
from grafo import Grafo
