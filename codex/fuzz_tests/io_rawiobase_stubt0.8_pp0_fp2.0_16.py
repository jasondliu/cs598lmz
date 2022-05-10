import io
class File(io.RawIOBase):
  def __init__(self, path=None, mode=None):
    pass
  def close(self):
    pass
  def fileno(self):
    pass
  def flush(self):
    pass
  def isatty(self):
    pass
  def readinto(self, b):
    pass
  def write(self, b):
    pass
  @classmethod
  def open(cls, path, mode=None):
    pass

class I2C:
    def __init__(self, bus, addr):
        pass

    def readfrom_into(self, address, buffer):
        return 0

    def writeto(self, address, buffer):
        return 0

    def writeto_mem(self, address, memaddr, buffer):
        return 0

    def readfrom_mem(self, address, memaddr, nbytes):
        return 0


class ADC:
    def __init__(self, id):
        pass

    def read(self):
        return 1024


class Pin:
    IN = 0
    OUT = 1

