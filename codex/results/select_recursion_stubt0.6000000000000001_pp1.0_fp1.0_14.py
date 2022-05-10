import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3

        def read(self):
            pass

    a.append(F())

    select.select(a, [], [], 0.1)

test_select_mutated()
</code>
The error message is:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python26\lib\threading.py", line 532, in __bootstrap_inner
    self.run()
  File "C:\Python26\lib\threading.py", line 484, in run
    self.__target(*self.__args, **self.__kwargs)
  File "C:\Python26\lib\subprocess.py", line 461, in _readerthread
    buf = read(fd, remaining)
ValueError: I/O operation on closed file
</code>
I have no idea how to fix this.


A:

The problem is that the subprocess module does not expect file descriptors to be closed during a <code>select</code> call.  It also does not expect the file descriptor to be
