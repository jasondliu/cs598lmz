import socket
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--host',help='host address',default='127.0.0.1')
parser.add_argument('--port',help='host port',default=12345,type=int)
parser.add_argument('--path',help='path to save file',default=os.getcwd())
args = parser.parse_args()

def recv_file(sock):
    #Receive file info
    file_info_size = struct.calcsize('128s32sI8s')
    buf = sock.recv(file_info_size)

    if buf:
        filename,temp1,filesize,temp2 = struct.unpack('128s32sI8s',buf)
        fn = filename.strip('\00')
        new_filename = os.path.join(args.path,fn)
        recvd_size = 0
        fp = open(new_filename,'wb')
        while not recvd_size == filesize:
            if filesize
