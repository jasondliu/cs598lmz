import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Python 3.2+
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.submit(lambda: sys.stdout.write('Hello World\n'))
