from types import FunctionType
list(FunctionType())

def arg(*args,**kwargs):
	from sys import argv
	from os.path import isfile
	return [ _[1:] if _.startswith("-") else _ for _ in argv[1:] ]

class Filetype:

	def __init__(self,**kwargs):
		from binascii import unhexlify
		from os.path import splitext
		from glob import glob
		from boottype import boottype

		self.MIME = {"FAT":"DOS/MBR","NTFS":"Windows/NTFS","EXT4":"EXT4","LEGACY":"LEGACY"}
		self.recordsize = {}
		self.hwdsize = {}
		self.SIZE_MB = 1000000
		self.SIZE_GB = 1000000000
		self.size = {"x86": { "max":{  "bytes":512,
																"max":self.SIZE_MB,
									
