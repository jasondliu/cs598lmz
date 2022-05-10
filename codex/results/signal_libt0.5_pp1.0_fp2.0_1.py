import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application window
window = Gtk.Window()

# When the window is given the "delete-event" signal (this is given
# by the window manager, usually by the "close" option, or on the
# titlebar), we ask it to call the delete_event () function
# as defined above. The data passed to the callback
# function is NULL and is ignored in the callback function.
window.connect("delete-event", delete_event)

# Here we connect the "destroy" event to a signal handler.  
# This event occurs when we call gtk_widget_destroy() on the window,
# or if we return FALSE in the "delete-event" callback.
window.connect("destroy", destroy)

# Sets the border width of the window.
window.set_border_width(10)

# Creates a new button with the label "Hello World".
button = Gtk.Button("Hello World")

# When the button receives the "clicked" signal, it will call the
# function
