import mmap
# Test mmap.mmap function
fileno = os.open('test.txt', os.O_RDONLY)
filemap = mmap.mmap(fileno, 0)
type(filemap)

# Just like in manual memory management, the data is freed automatically 
# upon garbage collection of the map instance, or when the with statement 
# is used to ensure the file is closed properly, which explicitly releases the memory.
# The map can be resized, moved and adjusted via the 
# underlying mmap module being exposed directly to the user.

filemap.size() # => 20

filemap.close() # => Causes the map to be unmapped and the memory freed

# Using spawn
# One thing you need to be careful when using the multiprocessing module 
# with the spawn initialization method is that some modules are not easily 
# pickled (such as modules related to network sockets).

# The fork method does not have this problem but does not work for Windows.
# The forking process works by copying all the virtual memory of the parent 
# process thus avoiding the need for pickling.
# The spawn method on the other
