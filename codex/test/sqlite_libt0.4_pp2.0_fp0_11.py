import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import traceback
import atexit

import xcb
import xcb.xproto
import xcb.render
import xcb.randr
import xcb.xinerama

import cairo
import pango
import pangocairo

import config
import util
import window
import theme
import hook
import layout
import bar
import widget
import command
import xcore
import xinerama
import xrandr
import xkb

class XScreen(xcb.xproto.Screen):
    def __init__(self, conn, screen):
        super(XScreen, self).__init__(conn, screen.root)
        self.conn = conn
        self.screen = screen
        self.root = screen.root
        self.default_colormap = screen.default_colormap
        self.white_pixel = screen.white_pixel
        self.black_pixel = screen.black_pixel
        self.root_depth = screen.root_depth
        self.root_visual = screen.root_visual
