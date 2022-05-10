import mmap
# Test mmap.mmap.read_byte
try:
    import thread
    import time
    f = open('/dev/null', 'w')
    m = mmap.mmap(f.fileno(), 0)
    m.write('abcde')
    t = thread.start_new_thread(m.read_byte, ())
    time.sleep(1)
    m.seek(0)
    for c in m: pass
    time.sleep(1)
except:
    print 'failed!'
