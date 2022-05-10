import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class GtkWidget(Gtk.Widget):
    __gtype_name__ = "GtkWidget"

    def __init__(self):
        Gtk.Widget.__init__(self)
        self.connect("expose-event", self.do_expose)
        self.set_size_request(100, 100)

    def do_expose(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_line_width(1)
        cr.set_source_rgba(1,1,1,1)
        cr.paint()
        cr.set_source_rgba(0,0,0,1)
        for i in range(25, 100, 25):
            cr.move_to(i, 0)
            cr.line_to(i, 100)
            cr.move_to(0, i)
            cr.line_to(100, i)
        cr.stroke()
        return False


class GtkWidget2(Gtk.Widget):
    __gtype
