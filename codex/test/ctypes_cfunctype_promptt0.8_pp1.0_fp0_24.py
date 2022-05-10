import ctypes
# Test ctypes.CFUNCTYPE
def t1(arg):
    pass
C = ctypes.CFUNCTYPE(None, ctypes.c_int)
type(C(t1))

import subprocess
class cmd:
    def __init__(self, args):
        self.args = args
        self.popen = subprocess.Popen(args, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
        self.fromchild = self.popen.stdout
        self.childerr = self.fromchild
    def close(self):
        self.fromchild.close()
        self.childerr.close()
        self.popen.wait()
    def __iter__(self):
        return self.fromchild

