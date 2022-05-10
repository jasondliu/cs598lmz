import sys, threading
threading.Thread(target=lambda: sys.stdout.write("WA\n")).start()
sys.exit(42)
