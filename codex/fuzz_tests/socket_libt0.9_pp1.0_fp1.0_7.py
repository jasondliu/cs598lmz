import socket
import struct
import subprocess
import sys


def usage():
    print "Usage: [your_path]/python EC2_Instance_Random_SSL.py [instance_id] [cert_folder_in_the_instance]"
    print "example: /home/my_id/python EC2_Instance_Random_SSL.py i-1234567890 /etc/ssl/test"


def get_host_ip4():
    """
    Get your local host ip, if you are on an invalid IP, then it will return None
    Return the local host ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    ip_ary = ip.split('.')

    if len(ip_ary) == 4:
        if not (ip_ary[0] == '10' or ip_ary[0] == '100' or ip
