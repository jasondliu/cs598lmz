import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Qt5 Webkit")

        self.browser = QWebView()
        self.browser.setHtml('''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <title>QWebView Example</title>
            </head>
            <body>
                <h1>Hello World</h1>
                <h2>This is a Test</h2>
            </body>
            </html>
        ''')
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
