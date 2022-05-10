import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets

from .windows import StateView, LampView

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class MultiState(QtCore.QObject):
    changed = QtCore.pyqtSignal(int)

    def __init__(self, pins, names):
        super().__init__()
        self.pins = pins
        self.sensor_states = [None] * len(pins)
        self.lamp_states = [False] * len(pins)
        self.update_all()

    def update_all(self):
        for i, pin in enumerate(self.pins):
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        while(1):
            for i, pin in enumerate(self.pins):
                state = GPIO.input(pin)
                self.sensor_
