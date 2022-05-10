import gc, weakref

from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.support import install_twisted_reactor
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationDrawer
from kivymd.uix.boxlayout import BoxLayout as MDBoxLayout
from kivy.uix.slider import Slider
from kivymd.uix.preicon import PreIcon
from kivymd.toast import toast
from kivymd.uix.screen import Screen
from kivymd.font_definitions import theme_font_styles

from twisted.internet import reactor, threads
from twisted.internet.defer import inlineCallbacks, Deferred
