import gc, weakref
import readline

import datetime

from freetype import *
from openpyxl import load_workbook, Workbook
from tkinter import *
from tkinter import ttk

import sys
sys.path.append('./gui/')
import gui_main

# global variables
global char_grid
global font_name, font_size, font_file
global sample_str, image_str
global uni_begin, uni_end
global char_height, char_width, char_size
global max_char_width
global font_list
global sample_str_opt

global output_folder
global style_name

global font_obj

global font_style
global font_code
global font_width

global output_font_name

global font_property

global progress_cur, progress_max

# GUI
global win, progress_var

def init():
    global char_grid
    global font_name, font_size, font_file
    global sample_str, image_str

    global uni_begin, uni
