import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)

central_widget = QWidget()
central_widget.setObjectName("central_widget")
window = QMainWindow()
window.setCentralWidget(central_widget)


def main():
    QtCore.QCoreApplication.setApplicationName("ModuleMixer")
    QtCore.QCoreApplication.setOrganizationName("LHPC")

    app = QApplication(sys.argv)

    show_gui(app)

    sys.exit(app.exec_())


def show_gui(app):
    Thread(target=make_window, args=(window, app)).start()


def make_window(window, app):
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()


if __name__ == "__main__":
    main()
