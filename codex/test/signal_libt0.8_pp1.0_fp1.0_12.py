import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

class FailuresDialog(Gtk.Window):
    def __init__(self, parent, title, label, failures):
        super(FailuresDialog, self).__init__()
        if parent:
            self.set_transient_for(parent)
        self.set_destroy_with_parent(True)
        self.set_border_width(5)
        self.set_title(title)
        self.set_default_size(400, 300)

        label = Gtk.Label(label=label)
        textview = Gtk.TextView()
        textview.set_editable(False)
        textview.set_cursor_visible(False)
        textview.get_buffer().set_text(failures)
        scrollable = Gtk.ScrolledWindow()
        scrollable.add(textview)

        button_box = Gtk.HButtonBox()
