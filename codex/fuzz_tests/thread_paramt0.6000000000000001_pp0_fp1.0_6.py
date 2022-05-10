import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]) + '\n')).start()

#
# from sys import argv
# from threading import Thread
# Thread(target=lambda: print('\n'.join(argv[1:]))).start()
#
# #
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]) + '\n')).start()
#
# #
# from sys import argv
# from threading import Thread
# Thread(target=lambda: print('\n'.join(argv[1:]))).start()
