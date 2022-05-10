import mmap
# Test mmap.mmap(0,1).size

m = mmap.mmap(0, 1)
try:
    oldSize = m.size()
    m.resize(1)
    if m.size() != 1:
        print(m.size(),1)
except OSError:
    print("mmap.size() not available")
else:
    m.resize(oldSize)
    # shouln't get an error, just make sure it doesn't crash
