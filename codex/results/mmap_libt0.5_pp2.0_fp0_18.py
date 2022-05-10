import mmap
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller
from pynput import mouse
import time
from datetime import datetime
import re
from os import path

# TODO:
#   - make a function to get the coordinates of a window
#   - make a function to get the coordinates of a window's close button
#   - make a function to get the coordinates of a window's minimize button
#   - make a function to get the coordinates of a window's maximize button
#   - make a function to get the coordinates of a window's restore button
#   - make a function to get the coordinates of a window's title bar
#   - make a function to get the coordinates of a window's bottom bar
#   - make a function to get the coordinates of a window's left bar
#   - make a function to get the coordinates of a window's right bar
#   - make a function to get the coordinates of a window's top-left corner
#   - make a function to get the coordinates of a window's top-right corner
#   - make a function to get the coordinates of a window
