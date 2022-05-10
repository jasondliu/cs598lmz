import socket
import struct

class GpioDriver(object):
    PIO_PINS = [23, 24, 25, 12, 16, 20, 21, 26]
    def __init__(self):
        self.set_up_gpio()
        self.current_values = []

    def set_up_gpio(self):
        GPIO.setmode(GPIO.BCM)
        self.on_list = [GPIO.LOW] * len(self.PIO_PINS)
        for pio in self.PIO_PINS:
            GPIO.setup(pio, GPIO.OUT)
            # initialize them to all off
            GPIO.output(pio, GPIO.LOW)

    def set_pio(self,index, value):
        """Set a GPIO to either HIGH or LOW"""
        GPIO.output(self.PIO_PINS[index], value)
        self.on_list[index] = value

    def toggle(self, index):
        """Toggle a GPIO between HIGH and LOW"""
        current_value = self.on_list
