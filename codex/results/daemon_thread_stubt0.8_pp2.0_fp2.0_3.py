import sys, threading

def run():
    p = subprocess.Popen(["python", "wslider.py"], stdin = subprocess.PIPE)
    global p1
    p1 = p
    p.stdin.write("k")
    while True:
        data = p.stdout.readline()
        if not data:
            print("NO")
            break
        else:
            print(data.strip())

def play(inp):
    p1.stdin.write(inp)

if __name__ == "__main__":
    t = threading.Thread(target = run)
    t.start()

    while True:
        stdin = sys.stdin.readline()
        if not stdin:
            break
        else:
            play(stdin)
        sys.stdin.flush()
