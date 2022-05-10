import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\r'+' '*40+'\r')).start()
import sys
for i in range(100):
    print i
    sys.stdout.flush()
    time.sleep(0.1)

sys.stdout.write('\r'+' '*40+'\r')

sys.stderr.write('Foo\n')

sys.stdout.write('\r'+' '*40+'\r')

sys.stdout.write('Done\n')

from IPython.core import ultratb
sys.excepthook = ultratb.FormattedTB(mode='Verbose', color_scheme='Linux', call_pdb=1)
import sys
class M(object):
    def __init__(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.stdin = sys.stdin

    def write(self, data):
        self.stdout.write('\r'+' '*
