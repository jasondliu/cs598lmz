import threading
# Test threading daemon run
def process_run(name):
    for i in range(5):
        print('Now %s is running.' % name)
        time.sleep(1)
    print('%s is finished\n' % name)


if __name__ == '__main__':
    # Create several threads
    t1 = threading.Thread(target=process_run, args=('process_1',))
    t2 = threading.Thread(target=process_run, args=('process_2',))
    t1.setDaemon(True)  # Set deamon
    t1.start()
    t2.start()
    t1.join()
    print('All threads are done.\n')
    print('The main thread will quit.')
    
# If there is no 'sys.exit(0)', the process will be killed automatically after terminated 'main thread' because 
# 'process_run' is a 'deamon thread'.
