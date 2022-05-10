import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale

from mainwindow import MainWindow
from settings import Settings

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("qgis-plugin-template")
    app.setOrganizationName("qgis-plugin-template")

    translator = QTranslator()
    translator.load(QLocale.system().name(), ":/translations")
    app.installTranslator(translator)

    settings = Settings()

    window = MainWindow(settings)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
