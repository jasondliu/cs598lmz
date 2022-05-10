import mmap
# Test mmap.mmap(id, length, access=mmap.ACCESS_WRITE) 

# Open file to mmap
f = open("test", "r+b") 
# f = open("test", "w+b") 

# Get mmap object
m = mmap.mmap(f.fileno(), 0) 
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) 

# Get string from mmap object
s = m.read(10) 
print(s)
print(type(s))

# Close file
f.close() 

# Close mmap object
m.close() 

</code>
The file test is a binary file with 10 bytes of data.
In the second case where access=mmap.ACCESS_READ, it works with no problem, but in the first case, I get an error:
<code>Traceback (most recent call last):
  File "t.py", line 20, in &lt;module&gt;
    s = m.read(10)
OS
