import socket
import sys
import threading
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class ChatBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.msg_list = []
        self.msg_list_box = BoxLayout(orientation='vertical', size_hint_y=None)  # Создаем вертикальный контейнер для сообщений
