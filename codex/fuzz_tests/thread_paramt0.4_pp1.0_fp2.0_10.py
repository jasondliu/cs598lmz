import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))

# Python 3:
import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(b'\n'.join(map(str.encode, range(100000)))))
</code>

