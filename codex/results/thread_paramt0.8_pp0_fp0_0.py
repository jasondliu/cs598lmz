import sys, threading
threading.Thread(target=lambda:sys.stdout.write(777), daemon=True).start()
print(8)

import sys, threading
threading.Thread(target=lambda:sys.stdout.write(888), daemon=False).start()
# print(9)

import sys, threading
threading.Thread(target=lambda:sys.stdout.write(999)).start()
# print(10)
