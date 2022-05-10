import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/yukon/ntv/testing/test.db')
import gc
import pdb

__author__ = 'YukonChen'

WHEEL_DELTA = 120

'''
ScrollView:
    TableLayout:
        GridLayout:
            orientation: 'vertical'

ScrollView:
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        GridLayout:
            cols: 2
            size_hint_y: None
            height: self.minimum_height

ScrollView:
    BoxLayout:
        GridLayout:
            cols: 2
            size_hint_y: None
            height: self.minimum_height

ScrollView:
    BoxLayout:
        GridLayout:
            cols: 2
            size_hint_y: None
            height: self.minimum_height

ScrollView:
    GridLayout:
        cols: 2
        size_hint_y: None
        height: self.minimum_height


ScrollView:

