import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QtGui.QApplication(sys.argv)
app.setOrganizationName("LM")
app.setOrganizationDomain("liuyangming.cn")
app.setApplicationName("TangPoem")
main_window = MainWindow()
main_window.show()
app.exec_()
