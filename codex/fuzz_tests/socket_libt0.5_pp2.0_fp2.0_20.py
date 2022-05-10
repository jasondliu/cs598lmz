import socket
import time
import os

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_mac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    mac = ":".join([mac[e:e+2] for e in range(0,11,2)])
    return mac

def get_time():
    localtime = time.asctime( time.localtime(time.time()) )
    return localtime

def get_osversion():
    osversion = os.popen("lsb_release -a").read()
    return osversion

def get_cpu():
    cpu = os.popen("cat /proc/cpuinfo | grep '
