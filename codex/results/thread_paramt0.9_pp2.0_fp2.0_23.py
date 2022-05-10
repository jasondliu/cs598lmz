import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(['%s is the process id.'%threading.get_ident() for x in range(100000)]) )).start()
