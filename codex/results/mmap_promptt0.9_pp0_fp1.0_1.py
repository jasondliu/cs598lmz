import mmap
# Test mmap.mmap(-1) is not NULL
mmap.mmap(-1, 0)
</code>
It's crashing with a Segmentation fault, but only on 32bit.
64bit systems work fine.
I use CentOS 6, Python 2.7 (64bit) and compiled Python 2.7.9 myself (32bit).
Note that I don't have any problems with mmap.mmap(fd, 0), only mmap.mmap(-1, 0)
What am I doing wrong?

Update:
I have tested on other linux distributions now, and all of them have the same problem.
Also, my conclusion about 32bit doesn't hold, on Fedora I have the same problem on 64bit (CentOS and Ubuntu work just fine).


A:

mmap.mmap(-1, 0) tries to use the tempfile library to allocate a temporary file. The documentation of the tempfile library suggests that it tries to fix a security issue by <code>fchmod(-1, 0666)</code> at line 120 of tempfile.py, when closing.
Perhaps I should check my version and upgrade.

