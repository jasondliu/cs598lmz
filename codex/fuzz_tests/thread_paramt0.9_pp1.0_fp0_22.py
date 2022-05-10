import sys, threading
threading.Thread(target=lambda: sys.stdout.write('a')).start()
threading.Thread(target=lambda: sys.stdout.write('b')).start()
threading.Thread(target=lambda: sys.stdout.write('c')).start()
threading.Thread(target=lambda: sys.stdout.write('d')).start()
threading.Thread(target=lambda: sys.stdout.write('e')).start()
threading.Thread(target=lambda: sys.stdout.write('f')).start()
threading.Thread(target=lambda: sys.stdout.write('g')).start()
threading.Thread(target=lambda: sys.stdout.write('h')).start()
threading.Thread(target=lambda: sys.stdout.write('i')).start()
threading.Thread(target=lambda: sys.stdout.write('j')).start()
threading.Thread(target=lambda: sys.stdout.write('k')).start()
threading.Thread(target=lambda: sys.stdout.write('l')).start()

