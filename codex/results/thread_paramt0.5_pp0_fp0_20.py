import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()
</code>

