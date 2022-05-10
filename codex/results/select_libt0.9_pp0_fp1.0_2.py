import select
import socket
import sys
import thread
import time
import datetime
import urllib.request
        
list_of_clients = []
dict = {}

def clientthread(conn, addr):
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print(addr[1],": ",message.decode())
                message_to_send = ""
                message_to_send = message.decode()
                message_to_send = message_to_send.split(":")
                #Broadcasting
                for client in list_of_clients:
                    if conn!=client:
                        data = raw_input()
                        client.send(data.encode())
        except:
            remove(conn)
    conn.close()

def send_message(username,message,conn,addr):
    conn.send(message.encode())
        

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send
