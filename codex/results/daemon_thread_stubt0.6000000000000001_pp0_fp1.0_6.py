import sys, threading

def run():
    for i in range(100):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print('main thread')
    time.sleep(1)
    if not t.is_alive():
        print('end')
        break

# main thread
# main thread
# main thread
# main thread
# main thread

# 0
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
# main thread
#
