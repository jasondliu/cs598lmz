import threading
# Test threading daemon
import time
import socket

# Global variables
# True if we are in debug mode, False if not
DEBUG = True

# True if we are in simulation mode, False if not
SIMULATION = False

# True if we are in remote mode, False if not
REMOTE = False

# True if we are in remote mode, False if not
events = []
events_lock = threading.Lock()

# List of external events
external_events = []
external_events_lock = threading.Lock()

# List of connections
connections = []
connections_lock = threading.Lock()

# List of full connections
full_connections = []
full_connections_lock = threading.Lock()

# List of available ports
ports = []
ports_lock = threading.Lock()

# List of available hosts
hosts = []
hosts_lock = threading.Lock()

# List of available nodes
nodes = []
nodes_lock = threading.Lock()

# List of available racks
racks = []
racks_lock = threading
