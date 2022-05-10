import weakref

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.core.audio import SoundLoader
from kivy.graphics import Line, Color, Rectangle
from kivy.graphics.transformation import Matrix
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty, ListProperty, BooleanProperty, ObjectProperty,
    ReferenceListProperty, StringProperty)
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget

from tetris_game import Tet
