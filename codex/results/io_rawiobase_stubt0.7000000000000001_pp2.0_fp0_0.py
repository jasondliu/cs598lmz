import io
class File(io.RawIOBase):
    def __init__(self):
        self.bytes_read = 0
    def read(self, n):
        self.bytes_read += n
        return b"\x00" * n

f = File()

# print(f.read(100))
# print(f.bytes_read)

f.seek(10)
print(f.tell())



# File = open("outfile.txt")

# with open("outfile.txt") as file:
#     contents = file.read()

# print(contents)


# for line in open("outfile.txt"):
#     print(line)

# file = open("outfile.txt")
# file.write("Hello, world!\n")
# file.write("Bye, world!\n")
# file.close()

# file = open("outfile.txt")
# print(file.read())
# print(file.read())
# file.close()

# file = open("outfile.txt", "r+")
# print(file.read
