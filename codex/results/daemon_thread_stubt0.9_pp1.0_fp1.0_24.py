import sys, threading

def run():
    app = QtGui.QApplication(sys.argv)
    startUi = StartUi()
    startUi.show()
    sys.exit(app.exec_())
    sys.exit()


if __na
