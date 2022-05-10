import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(b"b'print(\"Hello world\")'"))
