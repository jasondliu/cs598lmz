import threading
# Test threading daemon
def run():
    print('I am running')
    time.sleep(1)

def main():
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        t.join()

if __name__ == '__main__':
    main()
