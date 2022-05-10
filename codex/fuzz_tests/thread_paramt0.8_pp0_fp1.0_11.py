import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\033[31m')).start()

def main():
    print("This message is red")

if __name__ == '__main__':
    main()
