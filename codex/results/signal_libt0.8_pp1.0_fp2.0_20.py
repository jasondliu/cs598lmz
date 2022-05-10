import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication

# The following #defines allow us to use a dynamic name for the app, which
# is especially handy if using using multiple instances, e.g. for debugging,
# otherwise the name of the module containing the App class is used.
# This can now be overridden with the --name command line option,
def define_app_name(filename):
    # Get the name of the module containing the App class.
    f = os.path.splitext(os.path.basename(filename))[0]
    # ...and use it to define the app name.
    global App
    App = type(str(f), (QApplication,), dict(__module__=sys.modules[__name__]))
define_app_name(__file__)
