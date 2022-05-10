import sys, threading

def run():
    current_milli_time = lambda: int(round(time.time() * 1000))

    print('start time milliseconds:', current_milli_time())
    print('start time seconds:', time.time())
    
    time.sleep(5)

    print('end time milliseconds:', current_milli_time())
    print('end time seconds:', time.time())


def __main__():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        time.sleep(1)
        print('keep alive...')
        
__main__()
