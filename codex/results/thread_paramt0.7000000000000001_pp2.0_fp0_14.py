import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))

# p.27
import sys

class OutputRedirector(object):
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

def p(x):
    print '\n'.join(str(i) for i in range(x))
    print >>sys.stderr, 'range(%d)' % x

sys.stdout = OutputRedirector(sys.stderr)
p(3)

# p.30
import threading
def print_cube(num):
    print 'Cube: %d' % (num * num * num)

def print_square(num):
    print 'Square: %d' % (num * num)

if __name__ == '__main__':
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube,
