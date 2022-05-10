import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from . import utils
from . import config
from . import settings
from . import widgets
from . import dialogs
from . import tasks
from . import ui

class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id='com.github.lainsce.dockbarx')
        self.connect('startup', self.on_startup)
        self.connect('activate', self.on_activate)
        self.connect('shutdown', self.on_shutdown)

    def on_startup(self, app):
        self.settings = settings.Settings()
        self.settings.load()
        self.config = config.Config(self.settings)
        self.config.load()
        self.config.connect('changed', self.on_config_changed)

