import mmap
import re

# Finds File Storage Physical Address (FSPA)
# Warning - THIS IS A HACK, DON'T USE IT FOR ANYTHING IMPORTANT
# 
# Performs simple maths on the file offset of a given object in order to find FSPA.
# If a multipart object, will return a list of FSAPs for each part.
# If an object of a size multiple of the page size, will extrapolate page size from there instead.

def findfspa(filename, obj=None):
    if obj:
        f = open(filename, "r", errors="replace")
        print("Opening %s for inspection" % filename)
        print("Finding FSPA for object %s" % obj.name)
        try:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
                offset = s.find(obj.name)
                print("%s offset in file is %x" % (obj.name, offset))
                if not offset == -1:
                    offset += len(obj.name)
                   
