import mmap
# Test mmap.mmap()

#import os
#print 'Current process: %d' % os.getpid()

#filename = 'test.txt'
#print 'Forking...'
#pid = os.fork()
#if pid == 0:
#    # In the child process
#    f = os.fdopen(os.open(filename, os.O_CREAT | os.O_RDWR), "wb+")
#    f.write('new data from child')
#    f.flush()
#    m = mmap.mmap(f.fileno(), 0)
#    print 'In child: reading data: %r' % m.read(15)
#    m.seek(0)
#    m.write('child')
#    m.flush()
#    m.close()
#    f.close()
#    print 'In child: closing file'
#    sys.exit(0)
#else:
#    # In the parent process
#    m = mmap.mmap(-1, 0)
#    print 'In parent: reading data: %r
