import weakref

from gi.repository import GLib, GObject, Gtk

from . import utils
from . import _, ngettext


class ProgressDialog(Gtk.Dialog):
    __gsignals__ = {
        'cancelled': (GObject.SignalFlags.RUN_LAST, None, ()),
    }

    def __init__(self, parent, title, message, cancellable=False):
        super(ProgressDialog, self).__init__(
            title=title, parent=parent, flags=Gtk.DialogFlags.MODAL)
        self.set_transient_for(parent)
        self.set_resizable(False)
        self.set_border_width(6)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.set_response_sensitive(Gtk.ResponseType.CANCEL, cancellable)

        self.vbox.set_spacing(6)
        self.vbox.set_border_width(6)
