import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from electrum_mona.i18n import _
from electrum_mona.plugins import BasePlugin, hook
from electrum_mona_gui.qt.main_window import ElectrumWindow

import sys
import os

class Plugin(BasePlugin):

    def fullname(self):
        return 'QT Console'

    def description(self):
        return """Console for QT-specific commands."""

    def __init__(self, gui, name):
        BasePlugin.__init__(self, gui, name)
        self.win = None

    def requires_settings(self):
        return True

    def settings_widget(self, window):
        return EnterButton(_('Enter console'), self.enter_console)

    def enter_console(self, window):
        from electrum_mona import SimpleConfig
        config = SimpleConfig()
        if not self.win:
