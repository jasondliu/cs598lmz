import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        self.connect("delete-event", Gtk.main_quit)


    def on_button_clicked(self, widget):
        print("Hello World")
        self.callback()

    def set_callback(self, callback):
        self.callback = callback


def callback():
    print("In callback")

win = MyWindow()
win.set_callback(callback)
win.show_all()
Gtk.main()
</code>

