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
            for processor_idx in range(num_processors):
                processor = WorkerProcessor(file_path, results_queue, processor_idx)
                threads.append(Thread(target=processor.run, name=f"Processor:{processor_idx}"))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
    else:
        Log.log(Priority.debug, "Parameter file_path is invalid!")


class
