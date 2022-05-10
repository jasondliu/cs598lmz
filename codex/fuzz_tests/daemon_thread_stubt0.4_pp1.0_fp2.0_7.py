import sys, threading

def run():
    while True:
        try:
            print("[+] Starting server")
            os.system("python3 server.py")
            print("[-] Server crashed")
        except:
            print("[-] Server crashed")

threading.Thread(target=run).start()

while True:
    try:
        print("[+] Starting client")
        os.system("python3 client.py")
        print("[-] Client crashed")
    except:
        print("[-] Client crashed")
