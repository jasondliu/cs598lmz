import sys, threading
threading.Thread(target=lambda:sys.stdout.write('Test\r')).start()
exit(0)
