import mmap
# Test mmap.mmap
import mmap
f = open("hello.txt")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
m.find("Hello Python!")
12
m.find("python")
-1
m.close()
f.close()

# Test mmap.mmap
import mmap
f = open("hello.txt", "wb")
f.write("Hello Python! Hello World!")
f.close()
f = open("hello.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
m.readline()
'Hello Python! Hello World!'
m.seek(0)
m.write("abcde")
m.seek(0)
m.readline()
'abcde Hello World!'
m.close()
f.close()

# Test mmap.mmap
import mmap
f = open("hello.txt", "wb")
f.write("Hello Python! Hello World!")
