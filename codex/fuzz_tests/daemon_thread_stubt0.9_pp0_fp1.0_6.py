import sys, threading

def run():
    threading.Thread(target=client_serv).start()
    threading.Thread(target=other_serv).start()

def client_serv():
    GPIO.output(TRIGGER_CLIENT, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_CLIENT, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(RECEIVE_CLIENT) == 0:
        start = time.time()
        if start - stop > 0.00002:
            break

    while GPIO.input(RECEIVE_CLIENT) == 1:
        stop = time.time()
        if stop - start > 0.00002:
            break

    elapsed = stop - start
    C = elapsed * 343 / 2
    print('Distance Client: %.1f cm' % C)
    if C <= STOP_SIGN_LOWER_BOUND:
        global alarm, lock
        lock.acquire()
        alarm[0] = 2
        lock.release()
    else:
        global alarm
