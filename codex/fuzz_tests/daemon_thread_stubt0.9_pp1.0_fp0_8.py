import sys, threading

def run():
    i = 0
    while True:
        i += 1
        sys.stdout.write("\r[%s] %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i))
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("Done")
