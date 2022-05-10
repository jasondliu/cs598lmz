import ctypes
ctypes.cast(new_file.ctypes.data, ctypes.POINTER(roi_hdr))
# ctypes.pointer(roi_hdr)

import numpy as np

while 1:
	x = raw_input('Enter command: ')
	if x.strip() == 'exit':
		break
	print 'Command was:', x.strip()
	print 'res: ', new_file.shape
	print 'res: ', new_file.flat[0:8]
	print 'res: ', new_file.flat[8:32]
	print 'res: ', new_file.flat[32:64]
	print 'res: ', new_file.flat[64:96]
	print 'res: ', new_file.flat[96:128]
	print 'res: ', new_file.flat[128:160]
	print 'res: ', new_file.flat[160:192]
	print 'res: ', new_file.flat[192:224]
	print 'res: ', new_file.flat[224:256]
	print '
