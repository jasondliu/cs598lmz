import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc\x1b[4m4\x1b[24m56\x1b[4m8\x1b[24m9012 3456 7890\n')).start()
threading.Thread(target=lambda: sys.stdout.write('\x1b[3A\x1b[1000D')).start()
threading.Thread(target=lambda: sys.stdout.write('\x1b[3A\x1b[7C')).start()
threading.Thread(target=lambda: sys.stdout.write('\x1b[B\x1b[1000D')).start()
threading.Thread(target=lambda: sys.stdout.write('\x1b[4m4\x1b[24m56')).start()
threading.Thread(target=lambda: sys.stdout.write('\x1b[4m8\x1b[24m9012 3456 7890\n')).start()
</code>
It does only work when all threads exist sequentially. Multiple cursors
