import sys, threading

def run():
    os.system('python3 main.py')

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
