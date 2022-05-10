import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = gtk.Window()
window.set_title("Tree View")
window.set_size_request(200, 200)
window.connect("destroy", lambda q: gtk.main_quit())

# Create a TreeStore with one string column to use as the model
liststore = gtk.ListStore(str)

# Create the TreeView using liststore
treeview = gtk.TreeView(liststore)

# Create the TreeViewColumn to display the data
tvcolumn = gtk.TreeViewColumn('Column 0')

# Add tvcolumn to treeview
treeview.append_column(tvcolumn)

# Create a CellRendererText to render the data
cell = gtk.CellRendererText()

# Add the cell to the tvcolumn and allow it to expand
tvcolumn.pack_start(cell, True)

# Set the cell "text" attribute to column 0 - retrieve text
# from that column in liststore
tvcolumn.add_attribute
