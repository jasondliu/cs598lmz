import socket
import pickle
import threading
import random
import time
import os
import sys
import argparse
import signal
import math
import queue
import argparse

# Global variables

# Maps a node's id to its IP address
node_id_to_ip = {}
# Maps a node's id to its port number
node_id_to_port = {}
# Maps a node's id to its socket
node_id_to_socket = {}
# Maps a node's id to a list of its neighbors
node_id_to_neighbors = {}
# Maps a node's id to its graph distance from the source node
node_id_to_distance = {}
# Maps a node's id to its predecessor node in the shortest path
node_id_to_predecessor = {}
# Maps a node's id to a list of its neighbors
node_id_to_neighbors = {}
# Maps a node's id to a list of its neighbors
node_id_to_neighbors = {}
# Maps a node's id to a list of its neighbors
node_id_to_neighbors
