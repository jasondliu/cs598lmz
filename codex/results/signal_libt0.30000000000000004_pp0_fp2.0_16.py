import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(400, 200)

# Create a table to place the widgets
table = Gtk.Table(2, 2, True)

# Create first button
button1 = Gtk.Button(label="Button 1")
button1.connect("clicked", button_clicked, "1")

# Create second button
button2 = Gtk.Button(label="Button 2")
button2.connect("clicked", button_clicked, "2")

# Attach the buttons to the table
table.attach(button1, 0, 1, 0, 1)
table.attach(button2, 1, 2, 0, 2)

# Add the table to the main window
window.add(table)

# Show the window and the table
window.show_all()

# Start the main loop
Gtk.main()
