import io
# Test io.RawIOBase
vc = io.RawIOBase()
# Test io.BufferedIOBase
vc = io.BufferedIOBase()
# Test io.IOBase
vc = io.IOBase()
# Tests _io.FileIO
vc = _io.FileIO


# Test subprocess.Popen
class Popen(subprocess.Popen):
    def __exit__(self, exc_type, exc_value, traceback):
        self.kill()
        super().__exit__(exc_type, exc_value, traceback)


def test_subprocess_popen() -> None:
    p = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
    p.communicate()
    p = subprocess.Popen(
        ['ls'],
        executable='/bin/ls',
        bufsize=2,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        universal_newlines=True,
       
