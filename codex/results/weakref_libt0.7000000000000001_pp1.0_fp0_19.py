import weakref
import logging
import threading
from datetime import datetime
from collections import defaultdict
from typing import Dict, DefaultDict, Tuple, Optional, Any, List
from functools import partial
from queue import Queue
from itertools import count

import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty, ListProperty, \
    ReferenceListProperty, OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.settings import SettingString
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
