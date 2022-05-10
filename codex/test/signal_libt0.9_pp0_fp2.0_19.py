import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import launcher
launcher.run()
