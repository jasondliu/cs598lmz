import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass

