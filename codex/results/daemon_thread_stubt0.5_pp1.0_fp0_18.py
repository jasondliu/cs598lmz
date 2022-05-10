import sys, threading

def run():
    global b
    global t
    while True:
        if t.isAlive():
            b = True
            t.join()
        else:
            break

def main():
    global b
    global t
    b = False
    t = threading.Thread(target=run)
    t.start()
    sys.exit()

if __name__ == "__main__":
    main()
</code>
The output of the above is:
<code>$ python3.6 main.py
$
</code>

