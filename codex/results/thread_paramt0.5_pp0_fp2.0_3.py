import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# def f():
#     sys.stdout.write(input())
#
# threading.Thread(target=f).start()
