import mmap
# Test mmap.mmap
a = mmap.mmap(0, 1024, "MyMap") 
a.write("characters")
