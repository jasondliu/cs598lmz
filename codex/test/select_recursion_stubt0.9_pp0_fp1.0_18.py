import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10 + len(a)

    a.append(F())
    selector = select.poll()
    try:
        selector.register(a[-1])
    except IndexError:
        pass

# copied from Lib/test/test_telnetlib.py
def test_Telnet_write_eof(monkeypatch):
    import socket
    import sys
    import telnetlib
    import unittest
    monkeypatch.setattr(socket, 'socket', lambda *args, **kwargs: None)

    class FakeSock:
        def sendall(self, *args):
            pass

        def shutdown(self, *args):
            pass

        def fileno(self):
            return 42

        def close(self, *args):
            pass
    old_sock = socket.socket
    class WriterTest(telnetlib.Telnet):
        def write(self, data):
            # a copy of telnetlib.write but without EOF
            if not self.sock:
                raise EOFError('write() on write-closed connection')
           
