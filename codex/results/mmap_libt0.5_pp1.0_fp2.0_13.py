import mmap
import re

# Open a file
fo = open("/etc/passwd", "r+")

# mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT, offset=0)

# Map a file into memory
m = mmap.mmap(fo.fileno(), 0, access=mmap.ACCESS_READ)

# Read from a mmap'ed file
print "First line:", m.readline()

# Seek to the beginning of the file
m.seek(0)

# Print the first line
print "First line again:", m.readline()

# Seek to the beginning of the file
m.seek(0)

# Search the file
print "Searching:", m.find("root")

# Seek to the beginning of the file
m.seek(0)

# Find the first occurrence of a regular expression
print "First matching pattern:", m.readline(m.find(re.compile("root")))

# Close the mmap'ed
