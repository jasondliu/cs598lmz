import _struct
+
+class Packet:
+	def __init__(self, data):
+		self.packet = self.parse(data)
+		self.data = self.dump(self.packet)
+
+	def parse(self, data):
+		raise NotImplementedError
+
+	def dump(self, packet):
+		raise NotImplementedError
+
+class FSPPacket(Packet):
+	def __init__(self, data):
+		super().__init__(data)
+		self.protocol = self.packet[2:4]
+
+	def parse(self, data):
+		return _struct.unpack("<HII", data)
+
+	def dump(self, packet):
+		return _struct.pack("<HII", *packet)

