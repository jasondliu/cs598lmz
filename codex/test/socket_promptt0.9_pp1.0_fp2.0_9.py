import socket
# Test socket.if_indextoname(int(args.interface_index)).lower(), which is where it is used in fcntl.ioctl.

from odict import odict
from videooss import *
import videooss
import videooss_utils


import RTSP_CLIENT as RTSP




def usage(parser, code, msg=''):
    parser.print_help()
    return code

class VideoOSSClient:
    def __init__(self, repository_url, session_id, startconfig_file, binary='./videooss'):
        self.binary = binary
        self.startconfig_file = startconfig_file
        self.session_id = session_id
        self.repository_url = repository_url
        self.videooss_process = None
        
    def __del__(self):
        if self.videooss_process != None:
            self.videooss_process.kill()
