import select
import logging
from .lib import serial_ports


logger = logging.getLogger(__name__)


class Serial(object):

    def __init__(self, port, baudrate, config):
        self.connected = False
        self.config = config
        self.port = port
        self.baudrate = int(baudrate)
        self.serial = None
        self.port_open()
        self.connected = True

    @staticmethod
    def scan(config=None):
        return pyserial.tools.list_ports.comports()

    def port_open(self):
        """
        Opens the port. Timeout is setup in config.
        """
        self.serial = serial.Serial(
            self.port,
            baudrate=self.baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            xonxoff=0,
            rtscts=0)
        self.serial.timeout = self.config.get('timeout', 0.5)

    def
