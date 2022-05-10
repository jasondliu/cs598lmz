import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

#
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
#

#
# def _(o):
#     sys.stdout.write(sys.stdin.read())
# threading.Thread(target=_).start()
#
#
# def _(o):
#     return sys.stdout.write(sys.stdin.read())
# threading.Thread(target=lambda: _(0)).start()
#
#
#
#
# print "counter = {:d}".format(counter)
# print "counter = {:{align}{width}d}".format(counter, align='>', width='10')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

