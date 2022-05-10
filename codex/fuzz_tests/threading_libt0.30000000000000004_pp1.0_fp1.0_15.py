import threading
threading.stack_size(67108864) # 64MB stack

import sys
sys.path.append("/home/david/Documents/ClintonJail/Guccifer2.0/Docs&Tools/Python/ALL_GUC_FILE_PROJECT/python/modules/DOC")

from binarytoolkit import *

class doc_hdr_1(object):
	def __init__(self, file_object_):
		self.file_object = file_object_
		self.file_object.seek(0)
		self.data = self.file_object.read(2)
		
		self.wIdent = self.data[0:2]
		
		self.file_object.seek(2)
		self.data = self.file_object.read(2)
		
		self.nFib = self.data[0:2]
		
		self.file_object.seek(4)
		self.data = self.file_object.read(2)
		
		
