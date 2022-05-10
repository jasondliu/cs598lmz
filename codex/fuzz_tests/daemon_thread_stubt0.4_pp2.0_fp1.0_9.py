import sys, threading

def run():
    for i in range(5):
        print("Thread:", i)
        time.sleep(0.5)

if __name__ == "__main__":
    print("Start")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("End")

# Start
# Thread: 0
# Thread: 1
# Thread: 2
# Thread: 3
# Thread: 4
# End
