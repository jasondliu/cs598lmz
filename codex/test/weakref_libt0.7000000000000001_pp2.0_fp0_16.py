import weakref
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from leds import LED
from libs.color_utils import random_color, hsv_to_rgb
from libs.ui_utils import Button
from leds import LED_HORIZONTAL_COUNT, LED_VERTICAL_COUNT


class LEDWidget(Widget):
    def __init__(self, **kwargs):
        super(LEDWidget, self).__init__(**kwargs)
        self.scale = 0.5
        self.on_color = (1, 0, 0)
        self.off_color = (0, 0, 0)
        self.pos = (10, 10)
