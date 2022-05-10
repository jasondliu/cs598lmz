import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b""
    def write(self, b):
        pass

f = File()
print(f.read())

my_file = open("/tmp/foo.txt", "w")
my_file.write("Python is a great language.\nYeah its great!!\n")
my_file.close()

print(open("/tmp/foo.txt").read())

with open("/tmp/foo.txt") as f:
    for line in f:
        print(line, end="")

print("\n")

with open("/tmp/foo.txt") as f:
    print(f.readlines())

print("\n")

with open("/tmp/foo.txt") as f:
    print(f.read(8))

print("\n")

with open("/tmp/foo.txt") as f:
    print(f.read())

print("\n")

with open("/tmp/foo.txt") as f:
    print(f.read
