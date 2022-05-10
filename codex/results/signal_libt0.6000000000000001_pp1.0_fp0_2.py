import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.ui.textEdit.setText("Hello World!")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
</code>
Консольный вывод:
<code>&gt;&gt;&gt; import hello
QObject::connect: No such signal QPushButton::clicked(bool)
Q
