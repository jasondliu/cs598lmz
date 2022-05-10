import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
 
# Global variables
WIDTH = 480
HEIGHT = 800
STEP_TIME = 1./60.
 
# Initialise pygame (pygame crashes without the line below)
os.environ["SDL_VIDEODRIVER"] = "dummy"
 
# Initialise gtk, window and opengl
gtk.gdk.threads_init()
gtk.gdk.threads_enter()
gtk.main_init()
window = gtk.gdk.Window(None, width=WIDTH, height=HEIGHT,
    window_type=gtk.gdk.WINDOW_TOPLEVEL,
    wclass=gtk.gdk.INPUT_OUTPUT,
    event_mask=gtk.gdk.ALL_EVENTS_MASK)
 
# Initialise cairo
bitmap = gtk.gdk.Pixmap(window, WIDTH, HEIGHT)
cr = bitmap.cairo_create()
cr.set_
