import codecs
codecs.register_error("strict", codecs.ignore_errors)

class SwfFileWriter(object):
	def __init__(self, swfFile, swfVersion):
		self.swfFile = swfFile
		self.version = swfVersion
	
	def writeByte(self, byte):
		self.swfFile.write(struct.pack("B", byte))
	
	def writeUInt16(self, uint16):
		self.swfFile.write(struct.pack("<H", uint16))
		
	def writeUInt32(self, uint32):
		self.swfFile.write(struct.pack("<I", uint32))
		
	def writeFixed8(self, fixed8):
		self.swfFile.write(struct.pack("<h", fixed8))
		
	def writeFixed(self, fixed):
		self.writeUInt32(fixed * 65536)
		
	def writeString(self, string):
		if string == None:
			self.write
