import weakref

import gi
gi.require_version('GLib', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase

# Gst.debug_set_active(True)
# Gst.debug_set_default_threshold(3)

class GstPipeline(Gst.Pipeline):
    def __init__(self, *args, **kwargs):
        Gst.Pipeline.__init__(self, *args, **kwargs)
        self.bus = self.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', self.on_message)

    def on_message(self, bus, message):
        t = message.
