import mmap
# Test mmap.mmap
file=open("test.txt", "r+")
# size=os.path.getsize("test.txt")
size=100
m=mmap.mmap(file.fileno(), size)
m[0:len("hello")]="hello"
m.flush()
m.seek(0)
print "value is: ",str(m[0:len("hello")])
m.close()
