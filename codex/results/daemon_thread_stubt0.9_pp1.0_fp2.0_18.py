import sys, threading

def run():
    for i in range(0, 50):
        print threading.current_thread().name, threading.current_thread().ident, i
        time.sleep(random.randint(1, 2))   

thread1 = threading.Thread(target = run, name = 'thread1')
thread2 = threading.Thread(target = run, name = 'thread2')

thread1.start()
thread2.start()

thread1.join()
thread2.join()


# why threading? when is it useful to create own threads?
# uses a lot of threads. maybe lots of files or data.
# database, ip addresses, port number, all of these being modified at the same time.
# have threads for each of these so that all of these are being modified at the same time.
# creates a new process.
# keep in mind that threads also have what is called thread.lock so you can change
# the state at a certain time.

# PS threading is amazing. you can use it for anything.
# PS try to save a list inside a file and load it.
# PS:
