import threading
# Test threading daemon
import time
import spidev

class Trackball(threading.Thread):
    def __init__(self, spi_bus, spi_id, callback):
        threading.Thread.__init__(self)
        self.daemon = True
        self.running = False
        self.trackball = spidev.SpiDev()
        self.trackball.open(spi_bus, spi_id)
        self.trackball.mode = 3
        self.callback = callback
        self.events = {
            'up': [ 0xE, 0xF ],
            'down': [ 0xD, 0xE ],
            'left': [ 0xB, 0xC ],
            'right': [ 0x7, 0x8 ],
            'unmodified': [ 0xF, 0xF ]
        }

    def run(self):
        self.running = True
        while self.running:
            try:
                prev_val = 0xF
                for x in range(4):
                    val = self.trackball.xfer2([
