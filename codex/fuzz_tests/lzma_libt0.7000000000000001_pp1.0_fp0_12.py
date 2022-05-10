import lzma
lzmaCommands = [["xz", "xzdec"], ["lzma", "lzmadec"], ["unlzma", "lzmadec"]]
xzModes = ["--check=crc32", "--check=crc64", "--check=sha256"]

def getLzmaCommand():
	for cmd in lzmaCommands:
		if shutil.which(cmd[0]):
			return cmd[1]
	return None

def getLzmaModes():
	return xzModes

def decompressLzma(sourceFile, destFile, mode):
	cmd = [getLzmaCommand(), mode, sourceFile, "-so"]
	with open(destFile, "wb") as file:
		subprocess.check_call(cmd, stdout=file)

def compressLzma(sourceFile, destFile, mode):
	cmd = [getLzmaCommand(), mode, "-z", sourceFile]
	with open(destFile, "wb") as file:
		subprocess.check_
