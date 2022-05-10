import select
# Test select.select
def child(pipe):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = 'Spam %03d\n' % zzz
        os.write(pipe, msg.encode())
        zzz = (zzz + 1) % 5
def parent(pipe):
    while True:
        line = os.read(pipe, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
pipein, pipeout = os.pipe()
thread.start_new_thread(child, (pipeout,))
parent(pipein)

# Test thread.start_new_thread
import thread
stdout_mutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]
def counter(myID, count):
    for i in range(count):
        time.sleep(1)
