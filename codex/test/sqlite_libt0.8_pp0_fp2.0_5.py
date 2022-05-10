import ctypes
import ctypes.util
import threading
import sqlite3
import os.path

class MCP3008(object):

    def __init__(self):
        """SPI channel selection, defaults to channel 0"""
        self.channel = 0
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        #self.spi.max_speed_hz=1000000

    def analog_read(self, channel):
        """SPI read from MCP3008"""
        adc = self.spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

    def close(self):
        self.spi.close()

class SensorThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.code = None

    def run(self):
        print("Initializing MCP3008")
        mcp = MCP3008()
