import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#
# MainWindow
#
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__()

        # Create a new layout
        layout = QtWidgets.QVBoxLayout()

        #
        # Create a list of buttons
        #
        for i in range(10):
            layout.addWidget(Button('Button', lambda: self.buttonPressed(i)))

        #
        # Create the main widget and add the layout
        #
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    def buttonPressed(self, num):
        print('Button pressed {}'.format(num))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.
