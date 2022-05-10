import io
class File(io.RawIOBase):
	def __init__(self, filename):
		self.__filename = filename
		self.__name = "File({})".format(filename)
		self.__file = open(filename, "rb")

	def readinto(self, buf):
		return self.__file.readinto(buf)

	def close(self):
		self.__file.close()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

class Flasher:
	def __init__(self, port):
		self.__port = port
		self.__port.baudrate = 115200
		self.__port.bytesize = serial.EIGHTBITS
		self.__port.parity = serial.PARITY_NONE
		self.__port.stopbits = serial.STOPBITS_ONE
		self.__port.xonxoff = False
		self.__port.rtscts = False

