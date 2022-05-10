import select
import serial
import time
import threading

from control_window import Control
from pi.setup import GPIOSetUp
import config

class Cycle(threading.Thread):
    def __init__(self, pin_on, pin_off):
        threading.Thread.__init__(self)
        self.pin_on = pin_on
        self.pin_off = pin_off
        self.setup = GPIOSetUp()
        self.motor_running = False

    def stop(self):
        self.motor_running = False
        self.setup.close_gpio()

    def run(self):
        # Start gas valve
        self.motor_running = True
        self.setup.gpio_output_on(self.pin_on)
        while self.motor_running:
            self.setup.gpio_output_off(self.pin_off)
            time.sleep(config.UP_TIME)
            self.setup.gpio_output_on(self.pin_off)
            time.sleep(config.DOWN
