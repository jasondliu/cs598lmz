import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_title("Toggle Button")
window.set_default_size(200, 200)
window.connect("destroy", lambda w: gtk.main_quit())

# Create a toggle button
togglebutton = gtk.ToggleButton("Toggle Me")
togglebutton.connect("toggled", on_toggled)
window.add(togglebutton)

# Show the window and the button
window.show_all()
gtk.main()
