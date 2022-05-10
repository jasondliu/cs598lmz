import select
# Test select.select() and select.poll()
import time

# Example of the select function

def run_select_example():
    input = [1,2,3]
    output = [1,2,3]
    error = [1,2,3]
    timeout = 2
    readable, writeable, exceptional = select.select(
        input, output, error, timeout
    )
    print 'Timeout is set to', timeout, 'seconds'
    print 'returned objects are readable, writeable, exceptional'
    print readable
    print writeable
    print exceptional
    print '\n'

# Example of the select function
def run_poll_example():
    p = select.poll()
    print p.poll(1000)
    # Watch for read events on stdin
    p.register(sys.stdin, select.POLLIN)
    # Watch for read events on stdin and stdout
    p.register(sys.stdout, select.POLLIN | select.POLLOUT)
    # Watch for write events on stdout
    p.register(sys.stdout,
