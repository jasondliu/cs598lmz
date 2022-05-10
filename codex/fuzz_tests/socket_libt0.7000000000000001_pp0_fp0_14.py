import socket
import threading
from random import randint

from pymodbus.client.sync import ModbusTcpClient
import time

from PyQt5.QtCore import pyqtSignal, QObject


class Modbus(QObject):

    signal_change_values = pyqtSignal(list)

    def __init__(self, host, port, address_start=0, address_end=100):
        super().__init__()
        self.client = ModbusTcpClient(host, port)
        self.address_start = address_start
        self.address_end = address_end

    def run(self):
        while True:
            time.sleep(0.1)
            try:
                result = self.client.read_holding_registers(self.address_start, self.address_end - self.address_start,
                                                            unit=1)
                values = result.registers
                self.signal_change_values.emit(values)
            except Exception as e:
                print("Соединен
