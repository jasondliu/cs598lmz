import mmap
# Test mmap.mmap()
n = mmap.mmap(0,1)
print(n)
print(n.size())
print(n.readline())
print(n.readline())

for i in range(0,10):
    n.write("%d\n" % i)

n.seek(0)
print(n.readline())
print(n.readline())
print(n.readline())
print(n.readline())
print(n.readline())

print("----------------------------------------")

# Test mmap.mmap(file_handle
f = open("README.md","w+")
n = mmap.mmap(f.fileno(),0)

n.write("0123456789abcdefghijklmnopqrstuvwxyz\n")
n.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")

n.seek(0)
print(n.readline())
print(n.readline())

print("----------------------------------------")

# Test mmap.mmap
