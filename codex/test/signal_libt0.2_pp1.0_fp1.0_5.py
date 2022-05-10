import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)
window.set_default_size(400, 200)
window.set_title("Notebook")

# Create a Notebook, place the position of the tabs
notebook = Gtk.Notebook()
notebook.set_tab_pos(Gtk.PositionType.BOTTOM)
window.add(notebook)

# Let's append a bunch of pages to the notebook
for i in range(5):
    label = Gtk.Label("Page %s" % (i + 1))

    # Each page consists of a label and a close button
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    box.pack_start(label, True, True, 0)
