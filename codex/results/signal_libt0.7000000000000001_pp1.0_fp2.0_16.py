import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gio

from app import App

class Window(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_default_size(800, 500)
        self.set_border_width(5)

class Application(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id='org.example.myapp',
                         flags=Gio.ApplicationFlags.FLAGS_NONE,
                         **kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        app.app = App()
        win = Window(application=app)
        win.show_all()
        app.add_window(win)

app = Application()
exit_status = app.run(sys.argv)
sys.exit(exit_status
