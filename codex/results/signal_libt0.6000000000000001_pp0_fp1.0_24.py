import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import core
from . import client


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.state = core.State()
        self.client = client.Client(self.state)
        self.client.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(50)

    def on_timer(self):
        with self.state.lock:
            if not self.state.shutdown_event.is_set():
                self.state.shutdown_event.set()
                self.client.join()

                self.timer.stop()
                self.close()


def main():
    app = QApplication(sys.argv)
   
