import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
from mt19937 import MersenneTwister
rand = MersenneTwister(4)

class ROP(object):
	def __init__(self, binary, gadgets):
		self.binary = binary
		self.gadgets = gadgets

	def load(self, addr):
		global rand
		name = '%08x' % addr
		self.lib = ctypes.CDLL(name)
		fname = '.%s.fptr' % addr
		func = FUNTYPE(addr)
		func = func.__dict__['_FuncPtr__restype_']
		#setattr(self.lib, fname, func)

	'''
	def stack_align(self):
		addr = self.gadgets['call_ebx'][0]
		return addr
	'''

	def set_registers(self, eax=None, ebx=None, ecx=None, edx=None, esi=None, edi=None, ebp=None
