import mmap
# Test mmap.mmap
# 1. Create a file
f = open("testmmap.txt", "w+")
f.write("hello world")
f.close()
# 2. Open the file using mmap
f = open("testmmap.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
# 3. Read the file
print(m.readline())
# 4. Write to the file
m.seek(0)
m.write("hello world!")
# 5. Close the file
m.close()
f.close()


# Test mmap.mmap
# 1. Create a file
f = open("testmmap.txt", "w+")
f.write("hello world")
f.close()
# 2. Open the file using mmap
f = open("testmmap.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
# 3. Read the file
print(m.readline())
# 4. Write to the file
m.seek(0)
