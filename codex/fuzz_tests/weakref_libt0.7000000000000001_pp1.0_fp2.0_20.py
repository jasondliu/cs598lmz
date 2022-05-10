import weakref

from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation

import random
import time
import copy

# create GameScreen
Builder.load_file("GameScreen.kv")


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        self.input_box = None
        self.user_input = None
        self.start_time = None
        self.end_time = None
        self.diff = None
        self.score = None
        self.score_label = None
        self.pop
