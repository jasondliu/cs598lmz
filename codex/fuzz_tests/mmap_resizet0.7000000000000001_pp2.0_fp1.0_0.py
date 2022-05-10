import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # MemoryError

# results in
# Traceback (most recent call last):
#  File "test.py", line 11, in &lt;module&gt;
#    a = m[:] # MemoryError
# MemoryError
</code>

