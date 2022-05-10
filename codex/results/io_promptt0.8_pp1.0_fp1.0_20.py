import io
# Test io.RawIOBase class
r = io.RawIOBase()
print(r.read())
f = open('Text.txt','r')
w = open('write.txt','w')
w.write(f.read())
f.close()
w.close()
f = open('Text.txt','r')
print(f.read())
f.seek(0)
print(f.read(5))
f.seek(0)
print(f.readline())
print(f.readline(9))
f.seek(0)
for line in f:
    print(line,end="")
f.seek(0)
print(f.readlines())
f.seek(0)
print(f.writable())
#Test io.IOBase class
io.IOBase()
#Test io.BufferedIOBase class
io.BufferedIOBase()
#Test io.BytesIO class
io.BytesIO()
#Test io.StringIO class
io.StringIO()

#Test io.FileIO class
io.FileIO("Text.txt")

#Test io.Buff
