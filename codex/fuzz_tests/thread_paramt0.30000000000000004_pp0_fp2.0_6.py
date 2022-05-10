import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from . import main

if __name__ == '__main__':
    main()
