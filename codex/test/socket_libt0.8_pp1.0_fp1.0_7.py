import socket,os,threading
import queue
import hashlib

ip_port=('127.0.0.1',8001)
filelist=[]
filetranslist=[]
Back_log=5

def get_md5(filepath):
    if os.path.exists(filepath):
        BLOCK_SIZE=1024
        f = open(filepath, 'rb')
        md5_obj = hashlib.md5()
        while True:
            data = f.read(BLOCK_SIZE)
            if not data:
                break
            md5_obj.update(data)
        f.close()
        hash_code = md5_obj.hexdigest()
        return str(hash_code).upper()
    else:
        return "123"

class myserver(object):
    def __init__(self,recv_que,send_que):
        self.sk = socket.socket()
        self.sk.bind(ip_port)
        self.sk.listen(Back_log)
