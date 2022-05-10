import weakref

from collections import namedtuple

from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import Label as CoreLabel
from kivy.core.window import Window
from kivy.clock import Clock

from kivy.properties import StringProperty, NumericProperty, ObjectProperty, \
    ListProperty, BooleanProperty, OptionProperty

from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.snackbar import Snackbar
from kivymd.utils.cropimage import crop_image
from kivymd.utils.toolbar import Toolbar
from kivymd.uix.button import MDIconButton
from kivymd.theming import ThemableBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineIconListItem
from
