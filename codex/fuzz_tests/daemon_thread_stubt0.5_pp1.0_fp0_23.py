import sys, threading

def run():
    try:
        while True:
            threading.Thread(target=os.system("python3 ./main.py")).start()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

if __name__ == "__main__":
    run()
