import threading
# Test threading daemon.
def main(d):
    p = Popen(['./lccmatrixinv_omp'], stdin=PIPE, stdout=PIPE)
    for line in p.stdout:
        if line[:11] == 'Final Result':
            pass
    if p.poll() == None:
        p.kill() # If still alive, kill it.
    # Clean up
    p.stdout.flush()
    p.stdin.close()
    p.stdout.close()
    p.wait()
    if d > 0:
        global t
        t=threading.Timer(d, main, args=(d,))
        t.daemon = True
        print('Starting a new instance')
        t.start()
    else:
        print('No more tasks')
        time.sleep(2)

main(1)
while 1:
    time.sleep(1)
