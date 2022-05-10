import weakref

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from . import settings
from .utils import *

logger = logging.getLogger(__name__)

class Theme(object):
    def __init__(self, color='#000000', bgcolor='#ffffff',
                 text_color='#ffffff', text_disabled_color='#888888',
                 text_background_color='#000000',
                 scrollbar_color='#000000', scrollbar_background_color='#88
