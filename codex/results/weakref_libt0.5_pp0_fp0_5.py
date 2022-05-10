import weakref
from collections import defaultdict

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse, Line, PushMatrix, PopMatrix, Translate, Rotate
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.context_instructions import Color as ColorInstruction
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty, BooleanProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import
