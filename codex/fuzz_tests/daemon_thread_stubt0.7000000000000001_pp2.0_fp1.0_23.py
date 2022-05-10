import sys, threading

def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

def setup():
    run()

t = threading.Thread(target=setup)
t.start()
