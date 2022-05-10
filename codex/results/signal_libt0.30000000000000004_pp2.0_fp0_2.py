import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Load the Qt translation files
qtTranslator = QTranslator()
if qtTranslator.load("qt_" + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
    app.installTranslator(qtTranslator)

# Load the application translation files
appTranslator = QTranslator()
if appTranslator.load("translations/%s" % QLocale.system().name()):
    app.installTranslator(appTranslator)

# Create the main window
window = MainWindow()
window.show()

# Run the application
sys.exit(app.exec_())
