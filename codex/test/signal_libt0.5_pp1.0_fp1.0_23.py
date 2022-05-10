import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
