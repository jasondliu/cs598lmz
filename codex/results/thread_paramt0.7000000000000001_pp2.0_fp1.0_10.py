import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
</code>
Here's a version that works for files that are not plain text.
<code>import sys, threading
def read(file, buffer_size=4096):
    while True:
        buffer = file.read(buffer_size)
        if not buffer:
            break
        yield buffer
threading.Thread(target=lambda: sys.stdout.write(b''.join(read(sys.stdin.buffer)))).start()
</code>

