import mmap
# Test mmap.mmap

l = list(range(100))
print(l)

m = mmap.mmap(-1, 1024)    # create a memory-mapped file object
# negative num assume to buffer file is stdin/out/err
# pos num assume to buffer file the buffer file itself
# buffered file must be in binary mode 
m.write(os.linesep.join(str(s) for s in l))
m.seek(0)    # rewind file

result = [int(s) for s in m] # parse integers on mmap object

COLS = 10
for i, x in enumerate(result):
    print("%4i" % x, end="\n" if (i+1)%COLS==0 else " ")
print()

if __name__ == '__main__':
  pass
