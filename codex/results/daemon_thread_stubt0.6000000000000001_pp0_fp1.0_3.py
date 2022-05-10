import sys, threading

def run():
    sys.stdout.write('Hello from %s\n' % threading.current_thread())

def main():
    num_threads = int(sys.argv[1])
    threads = [threading.Thread(target=run) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

main()
