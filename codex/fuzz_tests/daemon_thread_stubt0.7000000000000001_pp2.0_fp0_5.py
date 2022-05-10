import sys, threading

def run():
    # this is the thread that we'll be running
    def foo():
        a = 0
        while True:
            a += 1
        
    # start the thread
    t = threading.Thread(target=foo)
    t.start()
    
    # wait for a keypress
    sys.stdin.read(1)
    
    # stop the thread
    t._Thread__stop()
    
    # wait for the thread to finish
    t.join()

if __name__ == '__main__':
    run()
