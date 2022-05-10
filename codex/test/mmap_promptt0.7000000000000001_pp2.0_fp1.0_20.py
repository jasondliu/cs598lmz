import mmap
# Test mmap.mmap.find
mf = mmap.mmap(0, 100, "testmmap")
mf.write("test")
mf.seek(0)
mf.find("test")
mf.find("test", 0)
mf.find("test", 1)
mf.find("test", 2)
mf.find("test", 3)
mf.find("test", 4)
mf.close()
# Test mmap.mmap.rfind
mf = mmap.mmap(0, 100, "testmmap")
mf.write("test")
mf.seek(0)
mf.rfind("test")
mf.rfind("test", 0)
mf.rfind("test", 1)
mf.rfind("test", 2)
mf.rfind("test", 3)
mf.rfind("test", 4)
mf.close()
# Test mmap.mmap.rfind
