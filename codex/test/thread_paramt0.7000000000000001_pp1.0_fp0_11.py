import sys, threading
threading.Thread(target=lambda: sys.stdout.write(raw_input('C'))).start()
raw_input('A')
sys.stdout.write('B')
