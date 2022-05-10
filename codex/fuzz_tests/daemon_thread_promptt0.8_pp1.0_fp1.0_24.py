import threading
# Test threading daemon


def func():
    num = 0
    while True:
        time.sleep(1)
        num += 1
        print(num)
        if num == 5:
            break


def main():
    t = threading.Thread(target=func)
    t.setDaemon(True)
    t.start()
    print("Here finish!!")


if __name__ == "__main__":
    main()
