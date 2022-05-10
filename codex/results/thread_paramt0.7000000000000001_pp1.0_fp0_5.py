import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(sys.stdin.read().split('\n')[::-1]))).start()
# my_first_thread.start()
