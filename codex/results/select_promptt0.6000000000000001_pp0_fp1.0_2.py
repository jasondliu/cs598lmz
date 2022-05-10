import select
# Test select.select()
# See http://docs.python.org/library/select.html

# Note: 
#   select.select() works on Windows, but not on Linux.
#   select.poll() should be used instead on Linux.

# Set up the data structures for polling
inputs = [ sys.stdin ]
outputs = [ ]

while inputs:
    print '\nPolling:', inputs
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    print '  readable:', readable
    print '  writable:', writable
    print '  exceptional:', exceptional
    
    for s in readable:
        if s is sys.stdin:
            data = sys.stdin.readline().strip()
            print '    Read (%d):' % len(data), data
        else:
            print '    Error:', s.getpeername()
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
    
    for s in writable:
        print '   
