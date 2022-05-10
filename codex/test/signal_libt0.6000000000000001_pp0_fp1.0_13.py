import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Batch Plot')

        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        self.create_main_layout()
        self.create_plot()

    def create_plot(self):
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy( QtCore.Qt.StrongFocus )
        self.canvas.setFocus()
        self.canvas.mpl_connect('key_press_event', self.on_key_press)
