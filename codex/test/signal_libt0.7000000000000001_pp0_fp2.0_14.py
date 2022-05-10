import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from . import data
#from . import data

from . import utils
from . import config

from .ui import main

from . import log

def main():
    # load config
    config.load()

    # init logging
    log.init_logging()

    # load data
    data.load()

    # start gui
    app = QtGui.QApplication(sys.argv)
    main = main.Main()
    main.show()
    sys.exit(app.exec_())

def _punch_in(project):
    # TODO: check if current project is the same
    data.current_project = project
    data.last_punch_in = datetime.datetime.now()
    data.save()

def _punch_out():
    data.last_punch_out = datetime.datetime.now()
    data.save()

