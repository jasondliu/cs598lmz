import threading
# Test threading daemon
def threading_daemon():
    name_of_thread = "Thread-{}".format(threading.currentThread().ident)
    print("[", name_of_thread, "] Started!")

    # Sleep for 3 minutes
    for i in range(1, 61):
        time.sleep(1)
        print("[", name_of_thread, "] Sleeping...")

    print("[", name_of_thread, "] Exiting...")

def main():
    threads_count = 5
    print("Number of threads:", threads_count)

    for i in range(0, threads_count):
        thread = threading.Thread(target=threading_daemon)
        thread.setDaemon(True)
        thread.start()

    # Sleep for 10 seconds to allow threads to complete
    time.sleep(10)
    print("Main thread exits...")

if __name__ == '__main__':
    main()

</code>
I get this result:
<code>Number of threads: 5
[ Thread-1397918348977
