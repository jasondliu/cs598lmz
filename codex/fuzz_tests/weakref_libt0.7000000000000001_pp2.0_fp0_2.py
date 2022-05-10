import weakref
import re
import math
import random
import time

try:
	import colorsys
except:
	print "unable to import colorsys"
	exit()

try:
	import cairo
except:
	print "unable to import cairo"
	exit()

try:
	import PIL
except:
	print "unable to import PIL"
	exit()

try:
	import pygtk
	pygtk.require("2.0")
except:
	print "unable to import pygtk"
	exit()
try:
	import gtk, gtk.glade
except:
	print "unable to import gtk"
	exit(1)

try:
	import gobject
except:
	print "unable to import gobject"
	exit()

try:
	import gtkmozembed
except:
	print "unable to import gtkmozembed"
	exit()

try:
	import gnome
	import gnome.ui
	import gnomevfs
except:

