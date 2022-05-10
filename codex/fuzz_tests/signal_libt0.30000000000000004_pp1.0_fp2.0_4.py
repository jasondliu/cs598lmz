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

# Create a button
button = Gtk.Button(label="Button 1")
button.connect("clicked", clicked)
grid.attach(button, 0, 0, 1, 1)

# Create a button
button = Gtk.Button(label="Button 2")
button.connect("clicked", clicked)
grid.attach(button, 1, 0, 1, 1)

# Create a button
button = Gtk.Button(label="Button 3")
button.connect("clicked", clicked)
grid.attach(button, 0, 1, 1, 1)

# Create a button
button
