import socket
socket.if_indextoname(3)

# 使用命令行
os.system('ifconfig')

import fcntl
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])

get_ip_address("ens33")


'''
#################################################################################
# 2.多线程
#################################################################################
'''

import threading
def thread_run():
    print("thread %s is running.." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

