import ctypes
import ctypes.util
import threading
import sqlite3
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5353))
s.listen(5)

def handle_new_client(conn, addr):
    global client_list
    print("Accepted connection from %s" % (str(addr)))
    client_list.append(conn)
    while True:
        data = conn.recv(1024)
        if not data:
            client_list.remove(conn)
            break
        for client in client_list:
            if client != conn:
                client.send(data)
    conn.shutdown()
    conn.close()
    print("Connection closed")

#----------------------------------------------------------------------
client_list = []
while True:
    client, addr = s.accept()
    new_thread = threading.Thread(target=handle_new_client, args=(client, addr))
    new_thread.start()
