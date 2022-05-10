import io
class File(io.RawIOBase):
    def readline(self, length=-1):
        return b'\n'

file = File()
 
print ("File==>",file.readline())
print ("File.isatty=>",file.isatty())
print ("File.isatty=>",file.readable())

#File==> b'\n'
#File.isatty=> False
#File.isatty=> True


#IOBase
    
print ("IOBase.isatty=>",file.isatty())
print ("IOBase.readable=>",file.readable())

#IOBase.isatty=> False
#IOBase.readable=> True

class File(io.RawIOBase):
    def readline(self, length=-1):
        return b'\n'

File.isatty = lambda self : True

file = File()
 
print ("File==>",file.readline())
print ("File.isatty=>",file.isatty())


# File==> b'\n'
# File.isatty=> True


