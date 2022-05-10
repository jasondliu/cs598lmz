import _struct
import ipaddress

# Global variables
HOST, PORT = "192.168.1.155", 2992
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
</code>


A:

Since you want 16 Bytes, you can use <code>_struct</code>:
<code>def packu64(v):
    packer = _struct.Struct('&lt;I')
    return packer.pack(int
