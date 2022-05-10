import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdin.readline()

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("done")

if __name__ == "__main__":
    main()
</code>

