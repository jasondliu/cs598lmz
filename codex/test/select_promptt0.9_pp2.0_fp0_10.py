import select
# Test select.select() using a pipe
r,w = os.pipe()
# Select only works on file descriptors, so we use os.fdopen
# to convert to file-like objects
r,w = os.fdopen(r,'r'), os.fdopen(w,'w',0) 

def writer():
    for i in xrange(5):                        
        time.sleep(1)                          
        w.write('%03d\n' % i)
