import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

# db = database.database()
dbc = database.data_base_connection()

app = QApplication(sys.argv)
app.setApplicationName('影城管理系統')
app.setWindowIcon(QIcon("./icon.png"))
main = Main()
main.show()
sys.exit(app.exec_())
