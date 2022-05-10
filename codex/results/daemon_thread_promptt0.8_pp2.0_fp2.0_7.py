import threading
# Test threading daemon
def daemon():
    while True:
        print('running ' + str(threading.current_thread().name) +'Process ' + str(os.getpid()))
        time.sleep(1)

d = threading.Thread(name='daemon', target=daemon)
d.start()
d.join()

# Multithreading 
def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())
def main():
    added_thread = threading.Thread(target= thread_job)
    added_thread.start()

if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=thread_job)
        thread.start()
    print('all done')

# Multithreading with args
def thread_job1(thread, a, b):
    print('This is an added Thread, number is %s' % threading.current_thread())
    print(a+b)

def main1():
    added_thread = thread
