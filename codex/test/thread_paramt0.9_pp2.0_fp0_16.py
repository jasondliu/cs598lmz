import sys, threading
threading.Thread(target=lambda: sys.stderr.write('%s\n' % '\n'.join(map(lambda s: s.strip(), open(__file__).readlines()[:15]))))
