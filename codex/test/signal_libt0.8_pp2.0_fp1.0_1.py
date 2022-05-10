import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from gi.repository import Gtk

from .window import Window


class App(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.gabmus.RopeGremlin",
                         **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = Window(application=self, title="RopeGremlin")
        self.window.present()


def main():
    app = App()
    app.run(sys.argv)


if __name__ == '__main__':
    sys.exit(main())
