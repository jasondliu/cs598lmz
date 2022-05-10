import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)
def showErr(errMsg):
    m = QtGui.QMessageBox()
    m.setText(errMsg)
    m.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("")
    app.setStyle(QtGui.QStyleFactory.create("plastique"))

    mw = QtGui.QMainWindow()
    mw.setWindowTitle("")
    mw.show()

    myWidget = MyWidget(mw)
    mw.resize(640,480)
    mw.setCentralWidget(myWidget)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
</code>


A:

The problem is in the way that you call <code>verticalScrollBar</code>. It should be <code>self.verticalScrollBar()</code>. 
After setting this, it works
