import mmap, time
from enum import Enum
from threading import Thread, RLock
from util import Log, Priority
from socket import socket, AF_INET, SOCK_STREAM
from os import path, name
from os import close as os_close
from queue import Queue, Empty


def start_processor(file_path: str, num_processors: int, results_queue: Queue):
    if file_path:
        if num_processors == 1:
            processor = WorkerProcessor(file_path, results_queue)
            processor.run()
        else:
            threads = []
