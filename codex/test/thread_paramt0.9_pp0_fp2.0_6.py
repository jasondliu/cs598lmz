import sys, threading
threading.Thread(target=lambda: (sys.stdout.write('thread\n'), sys.exit())).start()
main()
