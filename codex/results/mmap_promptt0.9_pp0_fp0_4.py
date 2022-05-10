import mmap
# Test mmap.mmap
#mkfiletest.py
#map = mmap.mmap(0, 1000, "test")
#map.seek(0)
#map.write("First line\n");
#map.write("First line\n");
#map.seek(0)
#result = map.readline();
#print "Should be First line"
#print result

#result = map.readline();
#print "Should be Second line"
#print result

#map.close()


# Test mmap.mmap class

#Mmap.py
import mmap

def make_map(filename):
    with open(filename, "w+") as f:
        # write 26 lines of "abc...xyz\n"
        for i in range(26):
            f.write(chr(i+97) * 10) # ten letters
            f.write("\n")
        f.flush()
        # memory-map the file, size 0 means whole file
        map = mmap.mmap(f.fileno(), 0)
        return map

# Use
