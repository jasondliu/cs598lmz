import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gtk.gdk

def get_win_pos(window):
    return window.get_position()

def get_win_size(window):
    return window.get_size()

def take_screenshot(x, y, w, h, filename_prefix, window=None):
    try:
        import Image
    except ImportError as e:
        try:
            from PIL import Image
        except ImportError as e:
            sys.stderr.write("Error: cannot import Image or PIL.Image\n")
            return
    screenshot = gtk.gdk.Pixbuf.get_from_drawable(gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, w, h),
                                                    gtk.gdk.get_default_root_window(),
                                                    gtk.gdk.colormap_get_system(),
                                                    x, y, 0, 0, w, h)

