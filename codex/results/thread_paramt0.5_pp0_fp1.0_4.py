import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(4, -1, -1)))))

# ***************************
# ***************************
# ***************************

# from __future__ import print_function
# import sys
# import threading
#
# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#     # print('Blastoff!')
#
# t = threading.Thread(target=countdown, args=(5,))
# t.start()
