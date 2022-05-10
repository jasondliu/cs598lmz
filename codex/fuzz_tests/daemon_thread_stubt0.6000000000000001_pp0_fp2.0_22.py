import sys, threading

def run():
    app = Application(sys.argv)
    app.exec_()

def start():
    thread = threading.Thread(target = run)
    thread.start()
</code>


A:

Qt is not thread safe, so you cannot use it from two different threads. This means that you have to have exactly one <code>QApplication</code> object, and all GUI access has to be done from its thread.
If you really want to use two threads, you need to use <code>QtCore.QObject.moveToThread()</code> to move each object to the thread it should live in.

