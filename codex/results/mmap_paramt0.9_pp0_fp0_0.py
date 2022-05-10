import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[0])
</code>
expected to print <code>1</code>, but it prints <code>63</code> instead.
If I add <code>flush=True</code> to <code>f.write</code>, it prints <code>1</code>, however I don't want the overhead.
I wonder what the problem is with my code?
EDIT
this was an issue on python 3, when compiled for windows (AND ONLY ON WINDOWS).
when compiled for UNIX, with <code>flush=True</code> the m[0] is <code>1</code>

