import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import gtk.gdk

def main():
    w = gtk.Window(gtk.WINDOW_TOPLEVEL)
    w.set_size_request(200, 200)
    w.connect("destroy", gtk.mainquit)
    w.show_all()

    filename = tempfile.mktemp(prefix='g-s-d-screenshot-', suffix='.png')
    w.window.property_change(
        gtk.gdk.atom_intern('_NET_WM_WINDOW_OPACITY', False),
        gtk.gdk.atom_intern('CARDINAL', False),
        8,
        gtk.gdk.PROP_MODE_REPLACE,
        [0xffffffff],
    )
    pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, 200, 200)
    pixbuf.get_from_drawable(w.window
