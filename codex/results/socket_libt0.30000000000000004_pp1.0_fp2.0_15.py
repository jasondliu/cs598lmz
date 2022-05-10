import socket
import sys
import time
import threading
import random
import os
import string

# Global variables
global_lock = threading.Lock()
global_time = 0
global_time_lock = threading.Lock()

# Global variables for the leader
global_leader_id = -1
global_leader_id_lock = threading.Lock()
global_leader_time = 0
global_leader_time_lock = threading.Lock()

# Global variables for the server
global_server_id = -1
global_server_id_lock = threading.Lock()
global_server_time = 0
global_server_time_lock = threading.Lock()

# Global variables for the client
global_client_id = -1
global_client_id_lock = threading.Lock()
global_client_time = 0
global_client_time_lock = threading.Lock()

# Global variables for the client
global_client_id = -1
global_client_id_lock = threading.Lock()
global_client_time = 0
global_client_
