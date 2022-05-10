import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# import sys
# import threading
# def print_newline():
#     sys.stdout.write('\n')
# threading.Thread(target=print_newline).start()
