import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk
import gobject

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(500, 300)
        self.connect("destroy", gtk.main_quit)
        self.webview = WebKit.WebView()
        self.webview.open("https://www.google.com/")
        self.add(self.webview)
        self.show_all()

if __name__ == "__main__":
    window = MainWindow()
    gtk.main()
