import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(int(input()))))+'\n')).start()

# from threading import Thread
# from sys import stdout
# from os import linesep
#
#
# def worker(n):
#     stdout.write('\n'.join(map(str, range(n))) + linesep)
#
#
# Thread(target=worker, args=(int(input()),)).start()

# from threading import Thread
# from sys import stdout
# from os import linesep
#
#
# def worker(n):
#     stdout.write('\n'.join(map(str, range(n))) + linesep)
#
#
# Thread(target=worker, args=(int(input()),)).start()
