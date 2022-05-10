import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", self.on_destroy)
        self.connect("key-press-event", self.on_key_press_event)
        self.connect("key-release-event", self.on_key_release_event)
        self.set_title("Keyboard events")
        self.set_size_request(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(250, 150)
        self.set_border_width(5)
        self.set_opacity(0.5)
        self.label = Gtk.Label("Press any key")
        self.label.set_size_request(100, 100)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.add(self.label)
        self.show_all()

    def on_destroy(self, widget):
