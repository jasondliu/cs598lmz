import sys, threading

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 50000))
    s.send(b"Hello, world")
    print(s.recv(1024))

    s.close()

def main():
    for i in range(100):
        t = threading.Thread(target=run)
        t.start()

if __name__ == "__main__":
    main()

#https://www.youtube.com/watch?v=bZr5MZ0rv5Y&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=6
