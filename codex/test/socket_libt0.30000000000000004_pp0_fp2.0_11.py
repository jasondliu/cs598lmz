import socket
import sys
import time
import threading
import json
import random
import os
import signal
import copy

#global variables
global_lock = threading.Lock()
global_var = {}
global_var['server_ip'] = '127.0.0.1'
global_var['server_port'] = 12345
global_var['server_socket'] = None
global_var['client_sockets'] = []
global_var['client_ips'] = []
global_var['client_ports'] = []
global_var['client_names'] = []
global_var['client_threads'] = []
global_var['client_thread_locks'] = []
global_var['client_thread_vars'] = []
global_var['client_thread_vars_lock'] = threading.Lock()
global_var['client_thread_vars_lock_list'] = []
global_var['client_thread_vars_list'] = []
global_var['client_thread_vars_list_lock'] = threading.Lock()
