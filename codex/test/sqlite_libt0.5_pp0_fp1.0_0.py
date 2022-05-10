import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import os
import sys
import json
import socket
import select

class Peer(object):
    def __init__(self, ip, port, peer_id, info_hash):
        self.ip = ip
        self.port = port
        self.peer_id = peer_id
        self.info_hash = info_hash
        self.last_seen = datetime.datetime.now()

class Torrent(object):
    def __init__(self, info_hash, name, tracker_url, tracker_port):
        self.info_hash = info_hash
        self.name = name
        self.tracker_url = tracker_url
        self.tracker_port = tracker_port
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)

class Tracker(object):
    def __init__(self):
        self.torrents = []
        self.torrents_lock = threading.Lock()
        self.db = sqlite3.connect
