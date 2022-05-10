import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#https://gist.github.com/csparpa/d8c9d30f1c89b2b7ebb8#file-pyqt5-matplotlib-multiaxes-example-py
class PyQt5_Matplotlib_MultiAxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
