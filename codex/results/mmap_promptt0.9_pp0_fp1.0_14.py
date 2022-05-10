import mmap
# Test mmap.mmap in read mode to see if the file exists and is > 0 bytes
f = open( 'mapfile.txt', 'w+')
f.write( 'asdf' )
f.seek( 0 )
m = mmap.mmap( f.fileno(), 0 )
print m.readline()
f.close()

# Here is where I get it to crash
m = mmap.mmap( f.fileno(), 0 )
```
gives:
```
python test_mmap.py 
Traceback (most recent call last):
  File "test_mmap.py", line 10, in <module>
    m = mmap.mmap( f.fileno(), 0 )
mmap.error: [Errno 9] Bad file descriptor
```
This is Python 2.7 on openSUSE 13.1.
Is there a way to set the mmap object to the None state when the file has either been closed or deleted?


A:

You just need to open the file in a context manager. As a result, when  the context is over, the undo stack
