import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.set_default_size(400, 200)
window.connect("delete-event", Gtk.main_quit)

# Create a table to place the widgets
table = Gtk.Table(3, 3, True)

# Create first button
button1 = Gtk.Button(label="Button 1")
button1.connect("clicked", print_hello)

# Create second button
button2 = Gtk.Button(label="Button 2")
button2.connect("clicked", print_hello)

# Place buttons in the grid
table.attach(button1, 0, 1, 0, 1)
table.attach(button2, 1, 3, 0, 1)

# Add the table to the main window
window.add(table)

# Show the window and run the app
window.show_all()
Gtk.main()
