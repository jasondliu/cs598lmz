import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass

try:
    import gtk
    import gtk.glade
except:
    print "gtk package not found\n"
    sys.exit(1)

"""set debugging"""
DEBUG = False
if "--debug" in sys.argv:
    DEBUG = True

if DEBUG:
    # setting default debug level to DEBUG if debugging
    from debuglog import *
    set_default_level(DEBUG_LEVEL_DEBUG)
else:
    from debuglog import *

"""daemon"""
class PCIDSK_GUI(PCIDSKDaemon):
    def __init__(self):
        PCIDSKDaemon.__init__(self)

        self.glade = "pcidsk_gui.glade"
        self.builder = None
        self.xml = None
        self.admin_main_window = None
        self.admin_new_
