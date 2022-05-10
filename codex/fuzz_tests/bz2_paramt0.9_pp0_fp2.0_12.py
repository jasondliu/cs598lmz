from bz2 import BZ2Decompressor
BZ2Decompressor('') # crash
t([1, 2]) # crash

# https://bugs.python.org/issue30467
from _tkinter import TclError as a
assert Tkinter is _tkinter # crashes
