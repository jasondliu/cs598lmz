import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

# from https://stackoverflow.com/questions/7088672/pyqt-thread-safe-call-to-a-gui-widget

# This class can be used to create a thread-safe call to a GUI widget.
#
# To use it, you need to subclass it and implement the run method.
#
# When you want to call a widget, just create an instance of your
# subclass, passing the widget as the first argument, and then call
# the start() method.
#
# If you need to pass arguments to the run method, just overload the
# constructor.
class GuiExecutor(QtCore.QObject):
    def __init__(self, fn, *args, **kwargs):
        QtCore.QObject.__init__(self)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @QtCore.pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)
