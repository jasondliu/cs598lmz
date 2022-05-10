import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def read_config(filename):
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read(filename)
    return config

def show_window(obj, title=None, size=None, position=None, maximized=False):
    """Show a QWidget object."""
    mw = qt.QApplication.mainWidget()
    if mw is None:
        mw = qt.QMainWindow()
        mw.setWindowTitle("pyFAI-GUI")
        mw.setWindowIcon(qt.QIcon(qt.QPixmap(IconDict["gioconda16"])))
    mw.setCentralWidget(obj)
    if title is not None:
        mw.setWindowTitle(title)
    if size is not None:
        mw.resize(size[0], size[1])
    if position is not None:
        mw.move(qt.QPoint(position[0], position[1]))

