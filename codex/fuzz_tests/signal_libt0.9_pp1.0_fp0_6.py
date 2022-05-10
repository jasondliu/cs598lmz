import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import Gtk
import Gtk.glade

class Label():
    '''A single label.
    '''
    def __init__(self):
        xml = Gtk.glade.XML(os.path.dirnam
