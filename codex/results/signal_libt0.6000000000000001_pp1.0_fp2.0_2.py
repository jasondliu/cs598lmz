import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(10)
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button(label="Hello")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button(label="Goodbye")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk
