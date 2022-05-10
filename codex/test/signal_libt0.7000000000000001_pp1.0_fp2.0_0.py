import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from .ui import MainWindow

def main():
	MainWindow()
