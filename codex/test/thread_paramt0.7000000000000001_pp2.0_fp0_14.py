import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))

# p.27
import sys

class OutputRedirector(object):
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

