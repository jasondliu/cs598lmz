import sys, threading

def run():
    global running
    while running:
        time.sleep(0.01)
        if time.time() - start_time >= 3:
            running = False

def main():
    global thread
    global start_time
    global running
    running = True
    thread = threading.Thread(target=run)
    thread.start()
    start_time = time.time()
    try:
        while running:
            pass
    except KeyboardInterrupt:
        pass
    print "exit"
    sys.exit(0)

if __name__ == "__main__":
    main()
