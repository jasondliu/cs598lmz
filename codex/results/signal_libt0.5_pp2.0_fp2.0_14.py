import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk

from kupfer.ui import keybindings, preferences, main

def main_window(options, args):
	"""
	Run the main window,
	returns when the window is closed
	"""
	preferences.load_preferences()
	keybindings.init_keybindings()
	mw = main.KupferWindow()
	mw.show_all()
	mw.present()
	gtk.main()

def main():
	"""
	Run main window
	"""
	import optparse
	parser = optparse.OptionParser()
	parser.add_option("-v", "--version", action="store_true",
			help="Show version")
	options, args = parser.parse_args()
	if options.version:
		print "Kupfer %s" % (__version__,)
		return
	main_window(options, args)

if __name__ == '__main__':
