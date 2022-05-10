import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows Ctrl-C in the terminal to kill the app.

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

app = QApplication(sys.argv)
w = QWidget()
w.resize(900, 600)
w.move(300, 300)
w.setWindowTitle('Basic Network Map')
w.setWindowIcon(QIcon('images/dove_icon.ico'))
labels = []
img = QPixmap("images/dove_icon.ico")  # Image should be square in pixels.

# This function redraws all the labels every 5 seconds.
def redraw_labels():
    del labels[:]
    # This loop places the network/host icons on the map.
