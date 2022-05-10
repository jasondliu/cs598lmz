import sys, threading

def run():
    while True:
        pass


def main():
    threading.Thread(target=run).start()
    while True:
        pass


if __name__ == "__main__":
    sys.exit(main())
