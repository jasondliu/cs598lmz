import io
class File(io.RawIOBase):
	pass

class NullFile(File):
	pass

# File "library.py"
import os
import shutil

def unlink(src, dst):
	if os.path.exists(dst):
		if os.path.isdir(dst):
			shutil.rmtree(dst)
		else:
			os.unlink(dst)
		message('unlink', dst)

def copy(src, dst):
	message('copy', src, dst)
	dstDir = os.path.dirname(dst)
	if dstDir and not os.path.exists(dstDir):
		message('dir', dstDir)
		os.makedirs(dstDir)
	shutil.copy(src, dst)

def link(src, dst, **kwargs):
	# retry with copy on EPERM
	try:
		message('link', src, dst)
		os.link(src, dst, **kwargs)
	except OSError
