import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView

# Create an instance of the application window and
# make it visible
app = QApplication(sys.argv)
app.setApplicationName('webview')

# Create QWebView object
web = QWebView()

# Resize web view to a specific size
web.resize(1024, 768)

# Load a web page into the web view
web.load(QUrl('http://www.kde.org/'))

# Show web view
web.show()

# Execute application
sys.exit(app.exec_())
