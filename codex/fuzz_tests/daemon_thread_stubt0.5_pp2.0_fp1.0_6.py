import sys, threading

def run():
    global r, g, b
    while True:
        if r < 255:
            r += 1
        else:
            g += 1
        if g > 255:
            b += 1
        if b > 255:
            r, g, b = 0, 0, 0
        time.sleep(0.01)

def main():
    global r, g, b
    r, g, b = 0, 0, 0
    t = threading.Thread(target=run)
    t.start()
    while True:
        print(r, g, b)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
