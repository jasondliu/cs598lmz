import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

class sgp4:
    def __init__(self):
        self.name = ''
        self.line1 = ''
        self.line2 = ''
        self.tle = None
        self.sat = None
        self.epoch = None
        self.tsince = None
        self.r = None
        self.v = None
        self.jd = None
        self.year = None
        self.mon = None
        self.day = None
        self.hr = None
        self.min = None
        self.sec = None
        self.az = None
        self.el = None
        self.range = None
        self.range_rate = None
        self.lat = None
        self.lon = None
        self.alt = None
        self.vel = None
        self.phase = None
        self.footprint = None
        self.orbit = None
        self.error = None
        self.opsmode = None
        self
