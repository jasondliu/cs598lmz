import sys, threading

def run():
    return

def main():
    num_threads = int(sys.argv[1])
    num_iterations = int(sys.argv[2])
    threads = []
    for i in range(num_threads):
        threads.append(threading.Thread(target=run))
    for i in threads:
        i.start()
    for i in threads:
        i.join()

if __name__ == "__main__":
    main()
