import weakref

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from . import utils
from . import widgets

class SelectableLabel(Label):
    def __init__(self, *args, **kwargs):
        self.register_event_type('on_double_tap')
        self.register_event_type('on_triple_tap')
        super(SelectableLabel, self).__init__(*args, **kwargs)
        self.long_press_time = 0.5 # seconds
        self.double_tap_time = 0.35 # seconds
        self.triple_tap_time = 0.35 # seconds
        self.last_touch_pos =
