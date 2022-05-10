import io
class File(io.RawIOBase):
	def read(self):
		return 1
		
# Create an instance of the class (policy #1)
f = File()
print(f.read())

# Use the class directly (policy #2)
print(io.RawIOBase.read(f))

# Or create a proxy that calls through to the instance (policy #1)
print(io.RawIOBase.read.__get__(f)())

# Or create a proxy that calls through to the class (policy #2)
print(io.RawIOBase.read.__get__(None, io.RawIOBase)())
