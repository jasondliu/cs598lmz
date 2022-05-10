import mmap
# Test mmap.mmap clean up
p = mp.Process(target=mmap.mmap)
p.start()
p.join()
