import mmap
# Test mmap.mmap
with open(filename) as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

lines = 0
readline = m.readline
while readline():
    lines += 1

print(lines)
</code>

EDIT:
The solution will be 
<code>import mmap
# Test mmap.mmap
with open(filename) as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

lines = 0
readline = m.readline
while readline():
    lines += 1

print(lines)
</code>

