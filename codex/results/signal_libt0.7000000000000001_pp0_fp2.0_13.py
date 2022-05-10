import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Screenshot(QObject):
  # The true code is at the end of each class
  def __init__(self, parent=None):
    super(Screenshot, self).__init__(parent)
    self.delay = 0
    self.completeScreenshot = QPixmap()
    self.lastRect = QRect()

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.raw_curses_screen = None
    self.raw_curses_screen_str = None
    self.raw_curses_screen_str_history = None
    self.raw_curses_screen_str_history_good = None
    self.last_raw_curses_screen_str = None
    self.last_raw_curses_screen_str_good = None
    self.last_raw_curses_screen_str_history_good = None
    self.curses
