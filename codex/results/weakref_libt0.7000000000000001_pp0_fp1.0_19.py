import weakref

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivy.graphics.context_instructions import Color, Rectangle

from kivymd.elevation import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior

from .tools import create_color_mask, get_color_from_hex
from .uix.dialogs import MDDialog
from .uix.label import MDLabel
from .uix.spinner import MDSpinner


def get_hex_from_color(color
