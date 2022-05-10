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
