import io
class File(io.RawIOBase):
	def writable(self):
		return True

	def write(self,data):
		print(data)
		return len(data)
file = File()
file.write(b"hello")
file.seek(0)
print(file.read())


class File(io.RawIOBase):
	def writable(self):
		return True

	def write(self,data):
		print(data)
		return len(data)
real_file = io.open("b.txt","w")
file = File()
file.write(b"hello")
file.seek(-5,io.SEEK_CUR)
print(file.read())
file.writelines(real_file)


class Mul(int):
	def __new__(cls,value):
		if not isinstance(value,int):
			value = int(value)
		return super(Mul,cls).__new__(cls,value)

	def __init__(self,value):
		self.value = value

