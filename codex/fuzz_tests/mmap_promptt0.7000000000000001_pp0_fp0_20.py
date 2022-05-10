import mmap
# Test mmap.mmap()
_mmap_f = os.open(file_path, os.O_RDWR)
_mmap_b = mmap.mmap(_mmap_f, 0)
_mmap_f.close()
_mmap_b.close()
# Test mmap.mmap() with anonymous mapping
_mmap_b = mmap.mmap(-1, 0)
_mmap_b.close()
# Test mmap.mmap() with access=mmap.ACCESS_COPY
_mmap_f = os.open(file_path, os.O_RDWR)
_mmap_b = mmap.mmap(_mmap_f, 0, access=mmap.ACCESS_COPY)
_mmap_f.close()
_mmap_b.close()
# Test mmap.mmap() with access=mmap.ACCESS_READ
_mmap_f = os.open(file_path, os.O_RDWR)
_mmap_b = mmap.mmap(_mmap_f, 0, access=
