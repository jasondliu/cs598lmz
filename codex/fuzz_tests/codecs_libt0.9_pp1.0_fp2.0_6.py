import codecs
codecs.register(mp3_support)


from kivy.app import App
from kivy.config import Config
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.vertex_instructions import Triangle
from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.garden.graph import Graph,
