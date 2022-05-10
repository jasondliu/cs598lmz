import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys, os, re

# - - -
# try importing core libs
try:
    import pygtk as gtk
    #gtk.set_interactive(False)
    #print "GTK+ version 2.0 or 2.2 found!"
    gtk_version = 2.0
    import gtk.glade
except:
    try:
        import gtk
        import gtk.glade
        import gtk.gdk
        #print "GTK+ version 2.4 or later found!"
        gtk_version = 2.4
    except:
        print "GTK+ not found! (http://www.pygtk.org/)"
        
try:
    import gnome
    #print "Gnome version 2.0 or later found!"
except:
    print "Gnome not found!"
    
try:
    import libglade
    print "libglade found!"
except:
    print "libglade not found! (http
