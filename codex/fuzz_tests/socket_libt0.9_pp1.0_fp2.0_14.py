import socket
		return socket.gethostbyname(socket.gethostname())
	else: return "192.168.1.127"

class IPAddress:
	def __init__(self):
		self.ip = self.getIP()

	def getIP(self):
		filename = config.usage.cacertfile.value
		if os.path.exists(filename):
			certfile = open(filename, "r")
			cacert = certfile.read()
			certfile.close()
			return getIP("3010", cacert)
		else:
			return getIP("3010")

class IPDevicesList:
	def __init__(self):
		self.ip = IPAddress().getIP()
		self.myList = []
		self.myList = self.getList()

	def getList(self):
		list = []
		devices = (self.ip.split(" ")[0])
		for device in devices.split("
