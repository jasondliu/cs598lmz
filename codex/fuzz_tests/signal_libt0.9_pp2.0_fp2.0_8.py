import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 

main = QApplication(sys.argv)
main.setApplicationName("Clinical Image Viewer")
main.setOrganizationName("ImageData")

mainWindow = QtGui.QMainWindow()
menuBar = createMenuBar(mainWindow)
mainWindow.setMenuBar(menuBar)

mainWindow.setWindowIcon(QIcon("Icon.ico"))

mainWindow.show()
main.exec_()
