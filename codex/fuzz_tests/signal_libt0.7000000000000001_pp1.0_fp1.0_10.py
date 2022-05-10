import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#create gui
app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
#main.show()
#main.resize(800, 600)
main.showFullScreen()

#load css
css = QFile(":/dark.qss")
css.open(QFile.ReadOnly)
main.setStyleSheet(QTextStream(css).readAll())

#start gui
sys.exit(app.exec_())
