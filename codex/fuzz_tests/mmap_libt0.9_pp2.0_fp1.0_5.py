import mmap
import os
import re
import sys

# this is needed for py2app/pyinstaller to work:
if getattr(sys, 'frozen', False):
    print('loading local modules...')
    path = sys._MEIPASS
    os.chdir(os.path.abspath(path))
    sys.path.insert(0, path)


from tkinter import filedialog, Label, StringVar, Tk
import tkinter.ttk as ttk
from tkinter.messagebox import askokcancel

from PIL import Image, ImageTk

from datetime import datetime
from string import ascii_uppercase

from utils import (
    _enumarate,
    _frame_bottom_border,
    _set_attributes,
    browse,
    convert_to_bbox,
    convert_to_bbox_label,
    convert_to_square_bbox,
    resize,
    save_config,
    show_img,
    size_to_max_dim,
)


# config
