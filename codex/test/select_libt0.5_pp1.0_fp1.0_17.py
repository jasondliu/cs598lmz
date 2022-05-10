import select
import socket
import sys
import threading
import time
from queue import Queue
from threading import Thread

from utils import *
from config import *
from socket_utils import *
from message import *
from membership_list import *
from failure_detector import *
from heartbeat import *
from membership_list import *
from failure_detector import *
from node_info import *

# Global variable
membership_list = MembershipList()
failure_detector = FailureDetector(membership_list)
heartbeat = Heartbeat(membership_list)

# Global variable for the file server
file_server_socket = None

# Global variable for the client
client_socket = None

# Global variable for the thread
threads = []

# Global variable for the join
is_join = False

# Global variable for the leader
is_leader = False

# Global variable for the leader
is_follower = False

# Global variable for the leader
is_candidate = False

# Global variable for the file server
is_file_server = False

#
