import threading
# Test threading daemon.
# https://stackoverflow.com/questions/13193278/understand-python-threading-daemon-possibility-to-not-wait-until-the-end-of-t

# Create some threads
def do_this(what):
    print (threading.currentThread(), what)
    time.sleep(1)

# Create some threads
def run_thread(what):
    thread = threading.Thread(target=do_this, args=(what,))
    thread.start()

if __name__ == "__main__":
    t1 = threading.Thread(target=do_this, args=("I'm function 1",))
    t2 = threading.Thread(target=do_this, args=("I'm function 2",))
    t1.start()
    t2.start()
    run_thread("I'm function 3")
    run_thread("I'm function 4")
