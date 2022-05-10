import select
import signal
import sys
import time

import pyperclip

import config
import errors
import log
import util

try:
    import colorama
    colorama.init()
except ImportError:
    pass

logger = log.get_logger()


class BaseClipboard(object):
    """
    Base clipboard class.
    """

    def __init__(self):
        self.clipboard_contents = None
        self.last_updated = None

    def get_clipboard_contents(self):
        """
        Get the current clipboard contents.
        """
        raise NotImplementedError

    def set_clipboard_contents(self, contents):
        """
        Set the clipboard contents.
        """
        raise NotImplementedError

    def get_clipboard_contents_if_changed(self):
        """
        Get the current clipboard contents if they have changed.
        """
        contents = self.get_clipboard_contents()
        if contents != self.clipboard_contents:
            self.clipboard_
