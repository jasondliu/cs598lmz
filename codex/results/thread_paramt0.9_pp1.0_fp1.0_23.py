import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\33]50;CurrentDir=' + os.getcwd() + '\a\n')).start()
# -
