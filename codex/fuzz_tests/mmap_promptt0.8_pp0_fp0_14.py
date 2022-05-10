import mmap
# Test mmap.mmap performance

fd = open("cmake_install_prefix.txt","r+")
mm = mmap.mmap(fd.fileno(),0)

# mm[:] = 'https://www.wikipedia.org/wiki/'
# mm.seek(0)
# print(mm.readline())

mm.close()
fd.close()

# mm = mmap.mmap(-1,1024)
# mm.write("Hello")
# mm.close()

# mm = mmap.mmap(-1,1024)
# mm.write("Hello" * 100)
# mm.close()

mm = mmap.mmap(-1,1024 * 1024 * 100)
mm[0:1024 * 1024 * 100] = "Hello" * 100
print(mm[0:1024])
mm.close()
