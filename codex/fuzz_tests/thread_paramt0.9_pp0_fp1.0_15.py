import sys, threading
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(1 % 4))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(100 % 8))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(14 % 27))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(84 % 3))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(33 % 2))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(203 % 100))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(53 % 10))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(5040 % 12))).start()
threading.Thread(target=lambda: sys.stdout.write("{}\n".format(6
