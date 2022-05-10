import gc, weakref

from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.transformation import Matrix
from kivy.graphics.texture import Texture
from kivy.resources import resource_find
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty, AliasProperty
from kivy.clock import Clock
from kivy.animation import Animation

from kivy.uix.image import Image
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
