import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

def do_something_else():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

def main():
    t = threading.Thread(target=do_something)
    t.daemon = True
    t.start()
    t.join()

    t = threading.Thread(target=do_something_else)
    t.daemon = True
    t.start()
    t.join()

if __name__ == '__main__':
    main()

# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
   
