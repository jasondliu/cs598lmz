import sys, threading
threading.Thread(target=lambda: sys.stdout.write('ABC')).start()
sys.stdout.write('DEF')
