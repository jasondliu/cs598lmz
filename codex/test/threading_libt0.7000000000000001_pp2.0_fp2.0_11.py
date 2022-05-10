import threading
threading.Thread(target=lambda: subprocess.check_call("python3 server.py", shell=True)).start()
threading.Thread(target=lambda: subprocess.check_call("python3 client.py", shell=True)).start()
threading.Thread(target=lambda: subprocess.check_call("python3 client2.py", shell=True)).start()
#threading.Thread(target=lambda: subprocess.check_call("python3 client3.py", shell=True)).start()
