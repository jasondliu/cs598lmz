import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import threading
from multiprocessing import Process, Queue
from pprint import pprint
import socket
import os

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')

from kivy.core.window import Window
Window.clearcolor = (0.7, 0.7, 0.7, 1)

from grpc.
