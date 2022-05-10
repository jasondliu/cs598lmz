import socket
import sys
import time
import datetime
import threading
import random
import os

# Global variables

# The number of clients that are connected to the server
num_clients = 0
# The number of clients that have sent the start signal
num_clients_start = 0
# The number of clients that have sent the stop signal
num_clients_stop = 0
# The number of clients that have sent the reset signal
num_clients_reset = 0
# The number of clients that have sent the exit signal
num_clients_exit = 0
# The number of clients that have sent the start signal
num_clients_start_ack = 0
# The number of clients that have sent the stop signal
num_clients_stop_ack = 0
# The number of clients that have sent the reset signal
num_clients_reset_ack = 0
# The number of clients that have sent the exit signal
num_clients_exit_ack = 0
# The number of clients that have sent the start signal
num_clients_start_nack = 0
# The number of clients that have sent the
