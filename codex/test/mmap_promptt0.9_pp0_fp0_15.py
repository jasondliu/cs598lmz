import mmap
# Test mmap.mmap function, using example from https://docs.python.org/2/library/mmap.html

import os
import sys
if sys.version_info[0] < 3:
    """On Python 2 stdout buffer may not be empty and the screen will be messed up, hence flush.
    https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
    """
    from IPython.utils.io import capture_output
else:
    from contextlib import redirect_stdout



class TestDocsExample:
    #https://docs.python.org/3/library/mmap.html
    def test_example(self):
        with open("example.db", "wb") as f:
            f.write(b"abc\n")
            f.write(b"def\n")

