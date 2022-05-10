import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

import csv
import os
import signal
import sys
import threading
from urllib.request import urlopen

from monzo import Monzo


class Indicator():
    def __init__(self):
        self.APPINDICATOR_ID = 'monzo_indicator'

        self.indicator = appindicator.Indicator.new(
            self.APPINDICATOR_ID, os.path.abspath('icons/default.svg'),
            appindicator.IndicatorCategory.OTHER)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

        self.populate_menu()
        self.update()
        notify.init(self.APPINDICATOR_ID)
