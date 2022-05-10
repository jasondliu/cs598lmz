import socket
import sys
import threading
import time
import tkinter as tk
import ttk

# Create the socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server.
sock.connect(("localhost", 10000))

# Create the thread that will receive messages from the server.
receive_thread = threading.Thread(target=receive)
# Daemonize the thread to stop it when the main thread ends.
receive_thread.daemon = True
# Start receiving messages.
receive_thread.start()

# Display the GUI.
root = tk.Tk()
root.title("Chat")
root.geometry("400x600")

messages_frame = tk.Frame(root)
my_message = tk.StringVar()
my_message.set("Type your messages here.")
scrollbar = tk.Scrollbar(messages_frame)
listbox = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar
