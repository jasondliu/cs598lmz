import sys, threading

def run():
    global p
    while True:
        try:
            p.stdin.write(sys.stdin.read(1))
        except IOError:
            break

def main():
    global p
    p = subprocess.Popen(sys.argv[1:], stdout=sys.stdout, stderr=sys.stderr, stdin=subprocess.PIPE)
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    p.wait()

if __name__ == "__main__":
    main()
