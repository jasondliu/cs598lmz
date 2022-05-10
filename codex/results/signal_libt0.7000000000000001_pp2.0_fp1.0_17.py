import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application window
window = Gtk.Window()

# Set the window title
window.set_title("TreeView")

# Set a handler for delete_event that immediately
# exits GTK.
window.connect("delete_event", Gtk.main_quit)

# Sets the border width of the window.
window.set_border_width(10)

# Create a new scrolled window, with scrollbars only if needed
scrolled_window = Gtk.ScrolledWindow()
scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Create a new tree model with 3 columns
# 0 - icon
# 1 - text
# 2 - color
liststore = Gtk.ListStore(str, str, str)

# Set the row data
liststore.append([Gtk.STOCK_APPLY, "APPLY", "green"])
liststore.append([Gtk.STOCK_C
