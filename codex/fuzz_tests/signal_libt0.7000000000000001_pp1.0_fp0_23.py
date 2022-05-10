import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import gobject
import gtk

from . import config

from . import plugin
from . import util
from . import window
from . import systray

from . import log
log = log.Log('main')

_instance = None

def init(options):
    global _instance
    assert _instance is None
    _instance = Exaile()
    _instance.init(options)

def main(options):
    init(options)
    gtk.main()

def quit():
    global _instance
    assert _instance is not None
    _instance.quit()

class Exaile(object):
    def __init__(self):
        self.started = False
        self.options = None
        self.windows = []
        self.tray = None

    def init(self, options):
        self.options = options
        if self.options.disable_plugins:
            self.options.disable_plugins = self.options.disable_plugins.
