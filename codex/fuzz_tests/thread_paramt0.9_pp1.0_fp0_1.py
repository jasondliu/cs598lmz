import sys, threading
threading.Thread(target=lambda: sys.stdout.write(''.join(map(lambda x: '%s, %x\n' % x, sorted((ord(c), c) for c in open(sys.argv[0]).read()))))).start()
