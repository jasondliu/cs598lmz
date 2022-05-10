import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
main_window = Gtk.Window()
main_window.set_title("Hello World")
main_window.set_default_size(200, 200)

# Create a label and put some text in it
label = Gtk.Label()
label.set_text("Hello World")

# Add the label to the main window
main_window.add(label)

# Connect the destroy signal of the window to gtk_main_quit
# When the window is about to be destroyed we get a notification and
# stop the main GTK+ loop
main_window.connect("destroy", Gtk.main_quit)

# Show the newly created widget
label.show()

# and the window
main_window.show()

# Start the main loop, and block until it finishes
Gtk.main()
