import sys, threading

def run():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))

    w = QtWidgets.QWidget()
    print(str(w))
    print(str(w.thread()))
    print(str(threading.current_thread()))
    w.show()
    app.exec_()

threading.Thread(target = run).start()
