import threading
threading.currentThread().setName("Main")

import sys, traceback, os, time, thread, ctypes

os.environ['PYSDL2_DLL_PATH'] = '../SDL2/lib/x64'

# import pyglet

import sdl2
import sdl2.ext

from dummysdlwindow import DummySDLWindow

import ctypes

from direct.showbase.ShowBase import ShowBase

from direct.gui.OnscreenImage import OnscreenImage

from direct.showbase.DirectObject import DirectObject

from direct.showbase import DirectObject
from panda3d.core import *

from panda3d.core import loadPrcFileData

loadPrcFileData("", "fullscreen t")

loadPrcFileData("", "win-size 1920 1080")
# loadPrcFileData("", "win-size 1280 720")
loadPrcFileData("", "win-origin 0 0")

loadPrcFileData("", "show-frame-rate-meter 1")
loadPrcFileData
