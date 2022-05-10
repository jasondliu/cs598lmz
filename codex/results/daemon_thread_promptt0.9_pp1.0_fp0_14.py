import threading
# Test threading daemon


def thread_function():
    while True:
        pass


def run_threads():
    threads = list()
    for index in range(30):
        threads.append(threading.Thread(target=thread_function))

    for thread in threads:
        thread.daemon = True
        thread.start()

    print(threads)

    time.sleep(3)
    print(threads)


if __name__ == '__main__':
    run_threads()
