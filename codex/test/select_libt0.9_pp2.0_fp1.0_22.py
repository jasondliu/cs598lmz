import select
import shutil
import subprocess
import time

from pywinauto import Desktop, Application
from pywinauto import keyboard
from pywinauto import mouse
from pywinauto.application import Application
from pywinauto.win32structures import RECT, POINT
from pywinauto.win32functions import BrowseDialog, OpenDialog

from . import __about__


def get_foreground():
    '''
    Get window handle and title of foreground window.
    '''
    return win32gui.GetForegroundWindow(), win32gui.GetWindowText(win32gui.GetForegroundWindow())


def find_by_name(name, **kwargs):
    '''
    Helper function to find window.
    '''
    return Desktop().window(**kwargs).wait('exists', timeout=10, retry_interval=1).wrapper_object()


