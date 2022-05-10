import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
window = gtk.Window()
window.set_title("Test")
window.connect("destroy", lambda q: gtk.main_quit())

# Create a table to place the widgets
table = gtk.Table(3, 3, False)

# Create a combobox
combo = gtk.combo_box_new_text()
combo.append_text("test")
combo.append_text("test2")
combo.set_active(0)
table.attach(combo, 0, 1, 0, 1)

# Create a progressbar
progressbar = gtk.ProgressBar()
table.attach(progressbar, 0, 1, 1, 2)

# Create a check button
check = gtk.CheckButton("Check me!")
table.attach(check, 0, 1, 2, 3)

