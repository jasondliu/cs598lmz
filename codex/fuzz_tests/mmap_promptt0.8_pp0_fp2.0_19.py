import mmap
# Test mmap.mmap()

mm = mmap.mmap(-1, 13)
mm.write("hello, world!")

print mm[:]

# Use mm[x:y] to slice an mmap object.
print mm[-5:]

mm.seek(0)
# Use find() to search the mmap'ed file.
print mm.find("wor")

# Use test to test the current position in the mmap'ed file.
print mm.tell()
print mm.size()

# Use close() to close the mmap object.
# It is not necessary to do this explicitly; it will be
# done for you when the mmap object is garbage-collected.
# However, if you want to map another file in its place,
# you must first close it.
mm.close()


# Test mmap.mmap()

mm = mmap.mmap(-1, 13)
mm.write("hello, world!")

print mm[:]

# Use mm[x:y] to slice an mmap object.
print mm[-5:]

mm.
