import socket, select, string, sys
import time
import random
import threading
import os
import json

if sys.version_info[0] != 2:
    print("You need python 2 to run this. For now at least.")

def pchat(name, connection, socklist):
    print("[+++] Opened new private chat with " + name)
    while True:
        try:
            message = input("> ")
        except:
            print("[---] Exiting private with " + name)
            priv.remove(connection)
            return s.sendto(bytes(json.dumps({"done":True}), "utf-8"), connection)
        if message:
            s.sendto(bytes(json.dumps({"message":message, "name":global_name}), "utf-8"), connection)
            sys.stdout.write(name + "(private): " + message + "\n> ")
            sys.stdout.flush()
        else:
            pass

def main():
    name = ""
    s = socket.socket(socket.AF
