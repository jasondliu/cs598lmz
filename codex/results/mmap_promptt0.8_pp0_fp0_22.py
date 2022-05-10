import mmap
# Test mmap.mmap
print("mmap.mmap: ", end="")
dic = mmap.mmap(-1, 128, "corpora.dic")
print("dic.read() = ", dic.read())
dic.close()
# Test mmap.mmap
print("mmap.mmap: ", end="")
dic = mmap.mmap(-1, 128, "test.dic", mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
dic.write("aaa")
print("dic.read() = ", dic.read())
dic.close()

print("Test completed")
