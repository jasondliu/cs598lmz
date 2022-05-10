import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

"""
	Entry point
"""
if __name__ == "__main__":

	glade_file = "../resources/glade/alarm.glade"

	builder = Gtk.Builder()
	builder.add_from_file(glade_file)

	main = MainController(builder)
	main.win.connect("destroy", on_win_destroy)

	main.win.show()

	Gtk.main()
