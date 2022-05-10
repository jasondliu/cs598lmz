from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def pack(self, *args):
	return struct.pack('i', *args)

s.pack = pack

import ctypes

class IntStruct(ctypes.LittleEndianStructure):
	_fields_ = [("data", ctypes.c_int)]

def convertInt(value):
	i = IntStruct()
	i.data = value
	return i.data

convertInt(65534)

import gc

def getStack():
	return [x.cell_contents for x in gc.get_objects() if type(x) == type(StackType.__new__(StackType))]

def findStacks():
	def _findStacks():
		for x in gc.get_objects():
			if type(x) == type(StackType.__new__(StackType)):
				if len(x.cell_contents) == 0:
					continue
				yield x.cell_cont
