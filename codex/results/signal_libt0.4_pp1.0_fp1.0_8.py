import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = gtk.Window()
window.set_title("Gtk.TreeView")
window.set_default_size(200, 200)
window.connect("destroy", lambda q: gtk.main_quit())

# Create a TreeStore with one string column to use as the model
treestore = gtk.TreeStore(str)

# We will add some data to the tree store.  Normally, you would
# probably create a custom class that subclasses TreeNode, fill
# an instance with data, and add the instance to the tree store.
# Here, we will just call the append() method of the tree store
# for simplicity.  We use some strings for the data.
treestore.append(None, ["Hello"])
treestore.append(None, ["World"])

# Now we will create the TreeView using treestore
# Just for fun, we will use multiple headers/columns
treeview = gtk.TreeView(treestore)

#
