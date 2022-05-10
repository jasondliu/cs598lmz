import mmap
# Test mmap.mmap()
fp = open("test_mmap.txt", "w+")
mm = mmap.mmap(fp.fileno(), 16 * 1024)
mm.write("hello world!")
mm.seek(0)
