import weakref

from pyglet.window import key

from ..core import *
from ..core import _keys


class _Keyboard(InputDevice):
    """Keyboard device.

    :Ivariables:
        `display` : `Display`
            Window that the keyboard is attached to.

        `modifiers` : dict of `Key` to bool
            Dictionary of the device's currently held modifiers.

        `pressed` : dict of `Key` to bool
            Dictionary of the device's currently pressed keys.
    """
    def __init__(self, display):
        self.display = display
        self._modifiers = {}
        self._pressed = {}
        self.open()

    def open(self):
        pass

    def close(self):
        pass

    def _process_window_event(self, symbol, modifiers):
        key_symbol = _keys.get(symbol, None)
        if key_symbol:
            self._modifiers[key_symbol] = bool(modifiers & key.MOD_CTRL)
