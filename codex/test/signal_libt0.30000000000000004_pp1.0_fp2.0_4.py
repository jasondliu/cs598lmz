import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.set_title("Grid")
window.set_default_size(400, 200)
window.connect("destroy", Gtk.main_quit)

# Create a grid
grid = Gtk.Grid()
grid.set_column_homogeneous(True)
grid.set_row_homogeneous(True)
window.add(grid)
