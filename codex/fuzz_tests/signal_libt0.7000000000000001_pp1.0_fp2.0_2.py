import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# run the main window

interface.main_window.mainloop()
