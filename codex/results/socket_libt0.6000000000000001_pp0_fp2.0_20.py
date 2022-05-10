import socket
import threading
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput

from game import Game
from player import Player
from settings import Settings


class ConnectPage(Screen):
    pass

class GamePage(Screen):

    def __init__(self, **kwargs):
        super(GamePage, self).__init__(**kwargs)
        self.game = Game()
        self.game.game_over_callback = self.on_game_over

        self.grid_width = self.ids.grid.width / Settings.GRID_SIZE
        self.grid_height = self.ids.grid.height / Settings.GRID_SIZE

        self.bind(on_enter=self.on_enter)

    def on_enter
