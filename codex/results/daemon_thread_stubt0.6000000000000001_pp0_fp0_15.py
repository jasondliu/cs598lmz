import sys, threading

def run():
    print("\033[1;32m[*]\033[0m Payload started")
    os.system("python3 -m http.server 80")

def connect():
    os.system("clear")
    print("\033[1;34m[*]\033[0m Connecting with the server")
    os.system("nc -lvp 8080")

if sys.argv[1] == "--server":
    try:
        run()
    except KeyboardInterrupt:
        print("\033[1;31m[*]\033[0m Payload stopped")
        sys.exit()

elif sys.argv[1] == "--client":
    try:
        connect()
    except KeyboardInterrupt:
        print("\033[1;31m[*]\033[0m Connection stopped")
        sys.exit()
