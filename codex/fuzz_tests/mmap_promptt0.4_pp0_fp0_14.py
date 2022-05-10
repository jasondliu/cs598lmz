import mmap
# Test mmap.mmap()
#
# On Windows, the length of a file opened with mmap.mmap() cannot be changed
# using mmap.mmap.resize().
#
# On Windows, mmap.mmap(0, length) maps the entire file.
#
# On Windows, mmap.mmap(0, length, access=mmap.ACCESS_WRITE) raises a
# ValueError.
#
# On Windows, mmap.mmap(0, length, access=mmap.ACCESS_COPY) raises a
# ValueError.
#
# On Windows, mmap.mmap(0, length, access=mmap.ACCESS_READ) raises a
# ValueError.
#
# On Windows, mmap.mmap(0, length, access=mmap.ACCESS_DEFAULT) raises a
# ValueError.
#
# On Windows, mmap.mmap(0, length, access=mmap.ACCESS_WRITE) raises a
# ValueError.
#
# On Windows, mmap.mmap(0, length, access=mmap.
