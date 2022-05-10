import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Try to load the Qt plugins from the local directory; if this fails,
# fall back to the standard library directory.
import os
import sys

# If the environment variable QT_PLUGIN_PATH is set, use it.
qt_plugin_path = os.environ.get('QT_PLUGIN_PATH')
if qt_plugin_path is not None:
    sys.path.insert(0, qt_plugin_path)

# If the environment variable QT_API is set, use it.
qt_api = os.environ.get('QT_API')
if qt_api is not None:
    sys.modules['PyQt4'] = __import__(qt_api)
    sys.modules['PyQt4.QtGui'] = __import__(qt_api + '.QtGui')
    sys.modules['PyQt4.QtCore'] = __import__(qt_api + '.QtCore')
    sys.modules
