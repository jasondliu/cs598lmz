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

# Add some values
combobox.append_text("Fedora")
combobox.append_text("Debian")
combobox.append_text("Ubuntu")
combobox.append_text("Arch")
combobox.append_text("Gentoo")

# Select one of the values (0-based)
combobox.set_active(0)

# Start the application
window.show_all()
Gtk.main()
