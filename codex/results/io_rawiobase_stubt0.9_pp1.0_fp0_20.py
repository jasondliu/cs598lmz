import io
class File(io.RawIOBase):
    def write(self, s):
        pass
#@+node:ekr.20031218072017.3252: * @file leoFileCommands.py
#@@language python
#@@tabwidth -4
#@+<<docstring>>
#@+node:ekr.20021021122818: ** <<docstring>>
""" Leo's core file-reading and file-writing routines.

Reading
========

Important note: Leo reads the body text at read time, not at the redraw
time.  This works because the body text is not c.p.v's
string.  The string is used only for undo/redo.

This code defines the Leo files that Leo can read.

@+at
#@nonl
#@-at
#@-<<docstring>>
#@+<< todo >>
#@+node:ekr.20031218072017.3255: ** << todo >>
#@@nocolor-node
#@+at
# 
# - The logic for reading and writing @last nodes should be moved to the
# proper chapter.
