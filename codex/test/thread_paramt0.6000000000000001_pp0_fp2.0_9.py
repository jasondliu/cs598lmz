import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(i) for i in range(10)))).start()
