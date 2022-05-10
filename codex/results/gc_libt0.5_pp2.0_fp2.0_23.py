import gc, weakref, sys
from types import MethodType
from weakref import WeakKeyDictionary
from functools import partial

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty, NumericProperty,\
    ListProperty, BooleanProperty, DictProperty
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.uix
