import sys, threading

def run():
    #print("Threading")
    for i in range(10):
        print("Threading")
        time.sleep(1)


def main():
    #print("Main")
    for i in range(10):
        print("Main")
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    main()
