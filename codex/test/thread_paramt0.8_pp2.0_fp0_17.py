import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(sys.path))).start()

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#from gi.repository import Gtk, Gd, Gdk, GdkPixbuf, GObject

#from gi.repository import Gtk, Gd, Gdk, GdkPixbuf, GObject

#from gi.repository import Gtk, Gd, Gdk
#from gi.repository import GdkPixbuf, GObject

#import datetime
import time

#from extensions_native.gi.repository.GdkPixbuf import Pixbuf
from gi.repository import GdkPixbuf
import os
import sys
#from PIL import Image
import pygame

#from gi.repository import Pango, PangoCairo
#from gi.repository import Pango
#from gi.repository import PangoCairo

from PIL import Image
