import sys, threading

def run():
    os.system("python3 server.py")

def main():
    t = threading.Thread(target=run)
    t.start()
    os.system("python3 client.py")

if __name__ == "__main__":
    main()
