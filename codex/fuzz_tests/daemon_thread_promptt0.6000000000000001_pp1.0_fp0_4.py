import threading
# Test threading daemon


def do_this():
    global x

    while x < 300:
        x += 1
    print(x)


def do_after():
    global x

    while x < 600:
        x += 1
    print(x)


def main():
    global x

    x = 0

    our_thread = threading.Thread(target=do_this, daemon=True)
    our_thread.start()

    our_thread2 = threading.Thread(target=do_after)
    our_thread2.start()

    print("Hello from main")


if __name__ == "__main__":
    main()
