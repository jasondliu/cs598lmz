import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# sys.stdout.write(sys.stdin.read())

# system('cat')

# import os
# os.execv('/bin/cat', ['/bin/cat'])
