import socket
import random
import time
from threading import Thread

NUM_OF_ICMPS = 5
NUM_OF_THREADS = 32


def generate_ip():
    """生成随机ip地址

    """

    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip


