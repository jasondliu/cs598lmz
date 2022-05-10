import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# load the window
window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(400, 200)
window.set_title("Keyboard Example")
window.set_border_width(5)

# create a box to hold everything
box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
window.add(box1)

# create a label to show the user what to do
label = Gtk.Label("Press any key to see it in the console")
box1.pack_start(label, True, True, 0)

# a text entry widget
entry = Gtk.Entry()
entry.set_text("Type here")
entry.connect("key-press-event", key_press_event)
box1.pack_start(entry, True, True, 0)

# show the window and run the app
window.show_all()
Gtk.main()
