import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.set_title("ComboBox")
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

# Create a ComboBoxText
combobox = Gtk.ComboBoxText()
combobox.connect("changed", on_changed)
window.add(combobox)

# Add some values to the ComboBoxText
combobox.append_text("Ubuntu")
combobox.append_text("Fedora")
combobox.append_text("Arch")
combobox.append_text("Gentoo")

# Select the first item
combobox.set_active(0)

# Show the window and all child widgets
window.show_all()

# Start the main loop
Gtk.main()
