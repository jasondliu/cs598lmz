import socket, select, string, sys, os
# import signal
# from multiprocessing import Process
# from threading import Thread
# from datetime import datetime
# from time import localtime, strftime

os.system('clear')
print ("[+] Starting server...")

# def signal_handler(signal, frame):
#     print('You pressed Ctrl+C!')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)


# --------------------------------
# ----------------- Config --------------
# --------------------------------

host = "0.0.0.0"
port = 4444
conn_num = 0
timeout = 20

# --------------------------------
# ----------------- Server --------------
# --------------------------------
def chat_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(10)
    print ("[+
