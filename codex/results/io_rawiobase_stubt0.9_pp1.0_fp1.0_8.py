import io
class File(io.RawIOBase):
    def __init__(self, what):
        if what != "file":
            raise OSError()
        pass

    def fileno(self):
        return 10

class Pty():
    # pty_make_controlling_tty() hangs after fork()
    def __init__(self):
        pass

    def openpty(self):
        return (10, 20)

    def fork(self):
        return 20

class BlockingIO():
    def __init__(self):
        self.__buffer = BytesIO()

    def write(self, what):
        while True:
            self.__buffer.write(what)
            break

    def read1(self, n):
        time.sleep(0)
        return self.__buffer.read(n)

def test_mesg_data_callback(dut, mesg_names, timeout=0.5, no_clear=False,
                            old_cr=None):
    """
    Calls the callback for each mesg name in the list, waits for timeout s to
    receive all
