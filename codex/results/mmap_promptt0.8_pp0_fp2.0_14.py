import mmap
# Test mmap.mmap

__author__ = 'Pawel'

map = mmap.mmap(0, 100, "mmaptest")

map.write("Hello world!")

map.seek(0)

print(map.read())

map.close()

print("DONE!")
