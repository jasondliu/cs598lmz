import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Clean up temp files.
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)

# Create a directory for the temporary files.
os.mkdir(temp_dir)

# Create a new window.
window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_default_size(600, 600)

# Create a new view.
view = gtk.TextView()
view.set_wrap_mode(gtk.WRAP_CHAR)

# Create a new buffer.
buffer = view.get_buffer()

# Connect the "changed" signal to the callback function.
buffer.connect("changed", changed_cb)

# Add the view to the window.
window.add(view)

# Show the window.
window.show_all()

# Start the main loop.
gtk.main()
