import sys, threading

def run():
    print('Threading Started')
    time.sleep(1)
    print('Threading Ended')

threading.Thread(target=run).start()

while True:
    print('Main Thread')
    time.sleep(0.5)

# Main Thread
# Main Thread
# Threading Started
# Threading Ended
# Main Thread
# Main Thread
# ^C
