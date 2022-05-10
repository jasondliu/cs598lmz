import mmap
# Test mmap.mmap on a file

# Open file and read in the whole thing
f = open('/etc/passwd','r')
content = f.read()
f.close()

# Open file and read in the whole thing using mmap
f = open('/etc/passwd','r')
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
m_content = m.read()
f.close()

# Compare contents
if content == m_content:
    print "mmap works!"
else:
    print "mmap doesn't work!"
</code>
The output of this is:
<code>mmap doesn't work!
</code>
I've seen some suggestions that this is because I'm using Windows and mmap isn't supported on Windows, but I'm using Python 2.7.9 on Mac OS X Yosemite.
Any ideas what I'm doing wrong?


A:

The problem is that you are using the <code>read()</code> method on the file object, not on the <code>mmap</code> object.

