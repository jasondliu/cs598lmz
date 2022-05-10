import io
# Test io.RawIOBase
print ("Test io.RawIOBase")
try:
    f = io.RawIOBase()
except:
    print ("io.RawIOBase failed")

fin = io.FileIO("fib.py", "r")
print (fin)
print ("Test getvalue")
x = "http://www.python.org"
f = io.StringIO(x)
print (f.getvalue())

print ("Test getvalue")
s = "abc"
buf = io.BytesIO(s.encode("UTF-8"))
print (buf.getvalue())

print ("Test linecache")
print (linecache.getline("fib.py", 3))

print ("Test linecache")
lines = linecache.getlines("fib.py")
for l in lines:
    print (l, end="")

print ("Test mmap")
f = open("fib.py", "r+b")
m = mmap.mmap(f.fileno(), 0)
m[0:10]
m.readline()
m.close()


