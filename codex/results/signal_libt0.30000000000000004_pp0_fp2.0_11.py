import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

# Create a table to place the widgets
table = Gtk.Table(3, 3, True)

# Create first button
button = Gtk.Button(label="Button 1")
table.attach(button, 0, 1, 0, 1)

# Create second button
button = Gtk.Button(label="Button 2")
table.attach(button, 1, 3, 1, 2)

# Create "Quit" button
button = Gtk.Button(label="Quit")
button.connect("clicked", Gtk.main_quit)
table.attach(button, 0, 3, 2, 3)

window.add(table)
window.show_all()

Gtk.main()
