import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(5)
    print('End daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('End non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading
def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    # added_thread.join()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == '__main__':
    main()
