import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from argparse import ArgumentParser

import yaml

from PyQt5 import QtCore, QtGui, QtWidgets

from . import __version__, __description__, __url__
from .gui import MainWindow
from .camera import Camera, CameraType
from .controller import Controller
from .model import Model


def read_config(filename):
    with open(filename, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    return config


def main(config):
    app = QtWidgets.QApplication(sys.argv)

    camera = Camera(CameraType.STREAM, config["camera"]["port"], config["camera"]["camera_number"])
    model = Model(config)
    controller = Controller(config)

    main_window = MainWindow(config, camera, model, controller)

    main_window.show()
    app.exec_()


