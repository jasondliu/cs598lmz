import mmap
# Test mmap.mmap()
filename = "home/luke/Desktop/test.txt"
#map = mmap.mmap(open(filename).fileno(), 0, mmap.MMAP_PRIVATE, mmap.MAP_SHARED)
map = mmap.mmap(open(filename).fileno(), 0)
index = map.find("\n")
end  = map.rfind("\n")
print(index)
print(end)
print(map[index:end])
map.close()
</code>
I get the error message:
<code>Traceback (most recent call last):
  File "/home/luke/anaconda3/lib/python3.6/site-packages/mmap.py", line 788, in __init__
    access, offset)
OSError: [Errno 22] Invalid argument

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "3.py", line 8, in &lt;module&gt;
    map = mmap.mmap(open(filename).
