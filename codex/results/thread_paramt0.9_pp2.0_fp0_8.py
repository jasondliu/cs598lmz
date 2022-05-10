import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Start Flask\r\n'), args=()).start()

import time
time.sleep(1)

threading.Thread(target=flask_init, args=()).start()

threading.Thread(target=bitmex.start_ws, args=()).start()

time.sleep(5)

threading.Thread(target=ws.start_ws, args=()).start()

time.sleep(10)

threading.Thread(target=start_trading, args=()).start()
