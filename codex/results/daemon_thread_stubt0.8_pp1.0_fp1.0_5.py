import sys, threading

def run():
    while True:
        try:
            config.main()
        except Exception as e:
            print("ERROR:", e)

def main():
    threading.Thread(target=run).start()

if __name__ == '__main__':
    main()
