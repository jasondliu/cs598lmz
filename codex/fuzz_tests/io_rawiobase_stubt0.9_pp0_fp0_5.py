import io
class File(io.RawIOBase):
	def readline(self):
		pass
	def write(self,data):
		pass

file = File()
file.readline()
class File(io):
	def readline(self):
		pass
	def write(self,data):
		pass

file = File()
file.readline()
import io
file = io.RawIOBase()
file.readline()

 
# end of the file
