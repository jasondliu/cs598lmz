import mmap
# Test mmap.mmap()

# Basically it's just a wrapper around mmap() that sets a few flags.

filename = "1.txt"

if os.path.exists(filename):
        os.remove(filename)

with open(filename, "w+") as f:
        f.write(b"Hello Python!")
        f.flush()

# Open the file
with open(filename, "r+") as f:
        # Memory-map the file, size 0 means whole file
        m = mmap.mmap(f.fileno(), 0)
        #print(type(m))
        #print(dir(m))

        # read content via standard file methods
        #print(m.readline())

        # read content via slice notation
        print(m[:5])  # prints "Hello"
        print(m[6:])  # prints "world!"

        # update content using slice notation;
        # note that new content must have same size
        m[6:] = b"python!\n"

        # ... and read again using standard file methods
