import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

"""
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=2)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
"""
IMG1_PATH = "D:\\opt\\_6C.bmp"

class SerialThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.dev_list = serial.tools.list_ports.comports()
	def run(self):
		self.ser = serial.Serial(port='COM3',baudrate=9600,timeout=None)
	def write(self, raw):
		self.ser.write(raw)

class BufferedImageSender(object):
	def __init__(self, img):
		if type(img) is str:
			self.img = Image
