import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.set_title("TreeView Demo")
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

# Create a TreeStore with one string column to use as the model
liststore = Gtk.ListStore(str)
for color in ["Red", "Green", "Blue", "Yellow"]:
    liststore.append([color])

# Create the TreeView using liststore
treeview = Gtk.TreeView(model=liststore)

# Create the TreeViewColumn to display the data
tvcolumn = Gtk.TreeViewColumn("Color")

# Add tvcolumn to treeview
treeview.append_column(tvcolumn)

# Create a CellRendererText to render the data
cell = Gtk.CellRendererText()

# Add the cell to the tvcolumn and allow it to expand
tvcolumn.pack_start(cell, True)

