import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebPage

class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

def main():
    url = 'http://webscraper.io/test-sites/e-commerce/allinone'
    r = Render(url)
    result = r.frame.toHtml()
    print(result)

if __name__ == '__main__':
    main()
