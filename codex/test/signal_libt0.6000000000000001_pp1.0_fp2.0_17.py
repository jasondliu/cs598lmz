import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import time
import gtk
import gtk.gdk
import gobject

import lib.xosd as xosd

#------------------------------------------------------------------------------

class Notify:

    def __init__(self, config):
        self.config = config

        self.timeout = 0
        self.timeout_id = None
        self.text = ""
        self.osd = None

        self.channel = self.config.channel
        self.channel.connect("notify", self.notify)

    def notify(self, channel, data):
        self.text = data.text
        self.timeout = data.timeout

        if self.timeout_id is not None:
            gobject.source_remove(self.timeout_id)

        self.timeout_id = gobject.timeout_add(self.timeout, self.timeout_cb)

        self.show()

    def timeout_cb(self):
        self.timeout_id = None
        self.timeout = 0
        self
