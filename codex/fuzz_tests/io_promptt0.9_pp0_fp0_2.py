import io
# Test io.RawIOBase
s = "hello world"
f = io.BytesIO(s.encode("utf-8"))
str = f.read(3)
f.seek(0)
str = f.read()
file = open("test.txt","w")
file.write("hello world")
file.close()

file = open("test.txt")
str = file.read()
file.close()

file = open("test.txt","wb")
file.write("hello world".encode("utf-8"))
file.close()

file = open("test.txt")
# raw buf to str
str = file.read().decode("utf-8")
# file.close()


with open("test.txt", "r") as f:
    str = f.read()

# if size is not set, default is 512
# if size not correct, you can use seek()
# tell() to return the current file
# position.

# io.TextIOBase subclass io.BufferedIOBase
# io.BufferedIOBase subclass io.IOBase

# io.Text
