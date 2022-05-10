import socket
import thread
import threading
import Queue

# The maximum number of threads to spawn.
# Each thread will handle one connection.
MAX_THREADS = 100

# The port to listen on.
LISTEN_PORT = 9999

# A global queue of incoming messages.
# This queue is shared among all threads.
incoming_queue = Queue.Queue()

# Maps from a socket (the key) to a list of messages (the value).
# Since TCP is a stream protocol, we have to buffer up messages
# until we see a newline.
socket_to_messages = {}

# Maps from a socket to a name.
socket_to_name = {}

# A lock used to synchronize access to the socket maps.
socket_maps_lock = threading.Lock()

# The set of sockets that we are listening to.
listen_sockets = set()

# The set of sockets that we are writing to.
write_sockets = set()

# The socket that we are listening to in the main thread.
server_socket = None

# The set
