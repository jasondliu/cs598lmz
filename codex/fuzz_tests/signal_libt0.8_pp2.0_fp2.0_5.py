import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

try:
    import krita
except ImportError:
    raise RuntimeError("Please run this script from Krita.")

from krita import Krita

import kritareinhard

"""
    This script provides a graphical user interface for adjustments
    of the color temperature and the exposure in Krita.
"""


class ColorTemperatureDialog(Gtk.Dialog):
    """
        This class provides methods to create and populate the dialog.
    """

    def __init__(self, app):
        """
            Initialize the dialog with a title and a button to apply the
            adjustment.
        """
        Gtk.Dialog.__init__(self, "Color Temperature", app.activeWindow(), 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)
