import ctypes
ctypes.windll.user32.ShowWindow(hwnd, 6) # 6 = SW_MINIMIZE
# ctypes.windll.user32.ShowWindow(hwnd, 3) # 3 = SW_MAXIMIZE
#ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# import sys
# import os
#
# # insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, os.path.join(sys.path[0], '..'))

import time
import logging
import pyautogui
import numpy as np
import cv2

from PIL import Image

from src.analysis.colors import is_red, is_green, is_yellow, is_blue

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

pyautogui.FAILSAFE = True

MAX_BOXES = 20

