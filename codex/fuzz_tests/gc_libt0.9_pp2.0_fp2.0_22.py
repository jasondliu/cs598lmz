import gc, weakref
from functools import partial

from kivy.logger import Logger
from kivy.core.image import Image as CoreImage
from kivy.resources import resource_find, resource_add_path, resource_remove_path
from path import path
from PIL import Image as PILImage

from pidev.kivy3 import GetObject
from pidev.kivy3 import PauseScreen
from pidev.stepper import stepper
from pidev.joystick import Joystick
from pidev.MixPanel import MixPanel
from pidev.Compass import compass
from pidev.droidcontroller import DroidController
from pidev.Cyprus_Commands import Cyprus_Commands_RPi
from pidev.Sphero_Controller import Sphero_Controller
from pidev.MixPanel import MixPanel
mixPanel = MixPanel("Project Name", "1.0", "abc123456789abc123456789abcdef12" )
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import
