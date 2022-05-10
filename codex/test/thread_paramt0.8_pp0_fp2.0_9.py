import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread2\n')).start()
sys.stdout.write('MainThread\n')
