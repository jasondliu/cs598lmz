import threading
threading.Thread(target=run_server).start()
time.sleep(1)

# Create a client
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

# Send a message
client.send(b"Hello\n")

# Receive a reply
reply = client.recv(1024)
print(reply)

# Clean up
client.close()
server.stop()
