import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
import os
import time
import re
import datetime
import traceback

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

import requests
from bs4 import BeautifulSoup

import mysql.connector

#from kivy.uix.widget import Widget
#from
