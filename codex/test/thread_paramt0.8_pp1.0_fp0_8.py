import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("Starting...\n")), daemon=True).start()
