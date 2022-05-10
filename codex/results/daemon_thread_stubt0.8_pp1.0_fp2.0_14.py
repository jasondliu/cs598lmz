import sys, threading

def run():
    print("[+] Thread ", threading.current_thread().getName(), " started")
    print("[*] Thread ", threading.current_thread().getName(), " is alive: ", threading.current_thread().is_alive())
    while threading.current_thread().is_alive():
        pass
    print("[*] Thread ", threading.current_thread().getName(), " is alive: ", threading.current_thread().is_alive())
    print("[*] Thread ", threading.current_thread().getName(), " is the main thread: ", threading.current_thread() == threading.main_thread())
    print("[-] Thread ", threading.current_thread().getName(), " started")
    sys.exit()

def main():
    print("[+] Starting Main thread")
    t = threading.Thread(target=run)
    t.start()
    print("[*] Is main thread alive: ", threading.main_thread().is_alive())
    print("[*] Is main thread daemon: ", threading
