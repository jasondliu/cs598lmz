import sys, threading
threading.Thread(target=lambda: sys.stdout.write("{} {}\n".format(n, n**2))).start()
threading.Thread(target=lambda: sys.stdout.write("{} {}\n".format(n**2, n))).start()
threading.Thread(target=lambda: sys.stdout.write("{} {}\n".format(n**2, n))).start()
