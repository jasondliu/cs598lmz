import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#create the main window
main_window = Gtk.Window( Gtk.WindowType.TOPLEVEL )
main_window.set_title("The Python GTK+3 Tutorial")
main_window.connect("destroy", main_quit)
main_window.set_default_size(500,500)
main_window.set_border_width(10)

def quit_cb( widget, data ):
    print( "Quit button clicked" )
    main_quit()

#create a button to put in the box
quit_button = Gtk.Button("Quit")
quit_button.connect("clicked", quit_cb)

#create a horizontal box
hbox = Gtk.HBox( True, 0 )

#create a button to put in the box
click_me = Gtk.Button("Click Me")
click_me.connect("clicked", quit_cb)

#create a vertical box
vbox = Gtk.VBox( True, 0 )

#create a
