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


def checksum(source_string):
    """ip数据报的校验和的计算：

    1.进行8位的分组，注意8位二进制不妨记为0xb
    2.对八位组计算溢出，如果两个8位组相加溢出了，就添加一个1，如果没有
