import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)
window.set_default_size(400, 300)
window.set_title("CellRendererSpin")

# Create a TreeStore with one string column to use as the model
liststore = Gtk.ListStore(str)
liststore.append(["1"])
liststore.append(["2"])
liststore.append(["3"])
liststore.append(["4"])
liststore.append(["5"])
liststore.append(["6"])
liststore.append(["7"])
liststore.append(["8"])
liststore.append(["9"])

# create the TreeView using liststore
treeview = Gtk.TreeView(model=liststore)

# create the TreeViewColumns to display the data
tvcolumn = Gtk.TreeViewColumn('Numbers')

# create a CellRendererText to
