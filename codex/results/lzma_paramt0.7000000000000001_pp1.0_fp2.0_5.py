from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''

def make_tar(path, name):
	with tarfile.open(name, "w:gz") as tar:
		tar.add(path, arcname=os.path.basename(path))
		print(path, "made tar")

def make_lzma(path, name):
	with LZMAInputFile(path) as f_in, LZMAOutputFile(name, format=FORMAT_ALONE) as f_out:
		shutil.copyfileobj(f_in, f_out)
		print(path, "made lzma")

def make_xz(path, name):
	with XZInputFile(path) as f_in, XZOutputFile(name) as f_out:
		shutil.copyfileobj(f_in, f_out)
		print(path, "made xz")

def make_7zip(path, name):
	with LZMAInputFile(path) as f_in, SevenZOutputFile(name, create_
