import io
class File(io.RawIOBase):
	def write(self,b):
		"""do nothing"""
		pass
	def read(self,size=-1):
		"""return null bytes"""
		return b""
nullFile=File()

# writes a whole file based on a list of strings and a file name
def writeFile(sList,fileName,append=False):
	f=open(fileName,
		"a" if append else "w")
	f.write("\n".join(sList))
	f.close()

# deletes a file if it exists
def deleteFile(fileName):
	if os.path.isfile(fileName):
		os.remove(fileName)

# returns the path to the bash script that executes commands
def getBashScriptPath():
	return os.path.abspath(__file__)

# returns the path to the shell script that sources the bash script
def getShellScriptPath():
	return os.path.dirname(getBashScriptPath())+"/sourceBash.sh"
	
def getFSKeywords
