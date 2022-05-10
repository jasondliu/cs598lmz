import sys, threading

def run():
    start = time.time()
    data = [random.random() for i in range(10**7)]
    print(time.time() - start)
    return data

def main():
    t = threading.Thread(target=run)
    t.start()

    t.join()

if __name__ == "__main__":
    main()
