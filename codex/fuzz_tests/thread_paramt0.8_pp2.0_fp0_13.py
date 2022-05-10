import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("\n\nPress a key to continue...\n"))).start()
