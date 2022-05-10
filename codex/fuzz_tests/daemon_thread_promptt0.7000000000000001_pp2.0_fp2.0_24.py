import threading
# Test threading daemon
def do_this():
    global x
    while True:
        x = x+1
        print x
        time.sleep(1)

def main():
    global x
    x = 0
    thread = threading.Thread(target=do_this, args=())
    thread.daemon = True
    thread.start()
    while True:
        pass
    return

main()
