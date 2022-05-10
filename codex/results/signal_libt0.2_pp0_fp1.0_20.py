import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

view = QWebEngineView()
view.load(QUrl("http://www.google.com"))
view.show()

sys.exit(app.exec_())
</code>
The above code works fine. But if I change the url to <code>http://www.google.com/maps</code> (or any other url that uses Google Maps), I get the following error:
<code>Qt WebEngine seems to be initialized from a plugin. Please set the QTWEBENGINE_CHROMIUM_FLAGS environment variable and restart.
</code>
I have tried setting the environment variable as suggested, but it doesn't help.
I am using Python 3.6.1 and PyQt 5.8.2 on Windows 10.

