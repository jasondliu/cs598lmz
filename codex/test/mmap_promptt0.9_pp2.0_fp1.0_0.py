import mmap
# Test mmap.mmap.resize() method, kernel pagesize handling.



# This will cause random failures - the resize test is very racy.  Skip it.
