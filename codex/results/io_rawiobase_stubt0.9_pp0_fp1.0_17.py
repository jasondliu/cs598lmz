import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode):
        self.file=open(file,mode)
    def close(self):
        self.close()
    def write(self, data):
        self.file.write(data)
    def fileno(self):
        return self.file.fileno()
    def read(self, size=-1):
        if size &lt; 0:
            size = 2**16
        return self.file.read(size)
</code>
Run that class as :
<code>file1 = File("1.txt","w+")
file2 = File("2.txt", "w+")
sys.stdout = file1
sys.stderr = file2

# Use print in the rest of your code
print("hello")
</code>


