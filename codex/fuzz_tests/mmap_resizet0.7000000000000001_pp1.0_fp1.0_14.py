import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
which results in a <code>ValueError</code> when trying to read the map.
I have tried closing the map with no success. I have tried using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> and <code>mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE)</code> with no success. I have tried using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> but that results in a <code>ValueError</code> when trying to truncate the file.
I'm looking for a way to truncate the file, preferably without copying the map (or at least without copying the entire map), and then continuing to use the map.
I'm using Python 3.4.2 (though I'm also interested in other versions, especially 2.x) on Ubuntu 14.04.

