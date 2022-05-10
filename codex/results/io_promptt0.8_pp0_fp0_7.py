import io
# Test io.RawIOBase
# fd = io.FileIO(str(0), 'r') # read from stdin
# fd = io.FileIO(str(1), 'w') # write to stdout
# fd = io.FileIO(str(2), 'w') # write to stderr
# fd.read(1) # read a single character
# fd.write(b'OK\n') # write OK and flush
# fd.flush()
# fd.readall() # read everything remaining
# fd.readall().decode('utf8')
# fd.readall() # must return b'' at EOF
# fd.close()
# fd.closed
# fd_2 = fd.__enter__()
# fd_2.close();
# fd.__exit__(None, None, None)
# fd.closed

#==============================================================================
# Test io.BufferedReader
# fd = io.FileIO(str(0), 'r') # read from stdin
# buf = io.BufferedReader(fd)
#
