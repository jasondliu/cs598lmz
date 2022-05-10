import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# # import threading
# def out():
#     sys.stdout.write(input())
# t1 = threading.Thread(target=out)
# t1.start()
