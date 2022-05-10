import weakref

from kivy.clock import Clock
from kivy.compat import PY2
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.widget import Widget

_modes = {}


def get_keyboard(win, *largs):
    if win not in _keyboards:
        return

    mode, mode_keyboard = _keyboards[win]
    if mode_keyboard is None:
        return
    return mode_keyboard.target


def list_keyboards():
    keyboards = []
    for win, (mode, mode_keyboard) in _keyboards.items():
        if mode_keyboard is None:
            continue
        keyboards.append(mode_keyboard.target)
    return keyboards


