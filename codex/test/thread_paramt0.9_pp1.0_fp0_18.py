import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()
import anyio
