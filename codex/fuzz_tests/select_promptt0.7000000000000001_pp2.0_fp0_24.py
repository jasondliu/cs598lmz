import select
# Test select.select() behavior on closed pipe.
# This would hang on Cygwin with Python 2.2.2
from subprocess import Popen, PIPE

# The following test would hang on Cygwin with Python 2.2.2
# See http://cygwin.com/ml/cygwin/2002-07/msg00487.html
def test_close_pipe():
    p = Popen(["cat"], stdin=PIPE, stdout=PIPE)
    p.stdin.close()
    select.select([p.stdout], [], [])
    p.stdout.close()

"""
def test_main(verbose=None):
    test_close_pipe()

if __name__ == "__main__":
    test_main(verbose=True)
"""
