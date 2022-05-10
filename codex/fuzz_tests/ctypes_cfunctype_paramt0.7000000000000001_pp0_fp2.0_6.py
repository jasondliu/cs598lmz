import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
import os
import weakref
from PyQt5 import QtWidgets


class KeyCombination(object):
    """
    Represents a hotkey combination.
    """

    def __init__(self, key, modifiers, callback):
        """
        Initialize the KeyCombination object.

        key: The key that is part of the hotkey combination.
        modifiers: A list of the modifiers that are part of the hotkey combination.
        callback: The function that will be executed when the hotkey is pressed.
        """
        self.key = key
        self.modifiers = modifiers
        self.callback = FUNTYPE(callback)
        self.id = None

        # Register the hotkey with the operating system
        self.register()

    def __del__(self):
        """
        Unregister the hotkey when this object is deleted.
        """
        self.unregister()

    def register(self):
        """
        Register the hotkey with the operating system.
        """
        modifiers = 0
        if 'ctrl' in self.modifiers:
            modifiers |
