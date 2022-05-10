import io
class File(io.RawIOBase):
    def close(self): print("close")
    def fileno(self): 1
    #def flush(self): print("flush")
    def read(self, n=-1): "row" if n < 0 else ("row"[:n])
    def seek(self, n, when=0): pass
    def tell(self): pass
    def write(self, b): print(b)
    def isatty(self): return False
#@
if False:  # verbose
    lines = []
    lines.append("""@
import sys
""")
    lines.append("""class oss(sys.stdout):
    def __init__(self):
        super(sys.stdout.__class__, self).__init__()
        self.name = 'o'
    def write(self, s):
        print("w", s, end="")
module_name = "arepl_module"
""")
    lines.append("""module_oss = oss()""")
    lines.append("""import sys
sys.stdout = module_oss
""
