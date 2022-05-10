import _struct
import serial
import time

from node import Node
from packet import Packet


class Arduino(Node):
    def __init__(self, name, serial_port, baud_rate):
        super(Arduino, self).__init__(name)
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.serial = serial.Serial(self.serial_port, self.baud_rate,
                                    timeout=1)
        self.serial.close()
        self.serial.open()

    def read_packet(self):
        packet_type = self.serial.read(4)
        if packet_type == 'DATA':
            source_node = self.serial.read(4)
            destination_node = self.serial.read(4)
            data = self.serial.read(4)
            packet = Packet(source_node, destination_node, data)
            return packet

    def write_packet(self, packet):
        self.serial.write('DATA')
