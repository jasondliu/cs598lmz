import socket
import hashlib
import urllib, urllib2
import utils

logger = logging.getLogger("soda-libs.socket")

class SocketHandler(object):
    """
    This class is the client socket handler
    """

    def __init__(self):
        #opener = urllib2.build_opener()
        #urllib2.install_opener(opener)
        #self.sessionId = str(hashlib.md5("soda-worker").hexdigest())
        self.sessionId = str("bcfda40d5fffe6f48c08f931cac8c1e1")
        logger.debug("SessionId -> %s" % self.sessionId)


    def sendData(self, data, conf=None):
        address = conf.get("address")
        port = conf.get("port")
        stage = conf.get("stage")
        try:
            if(address is not None and port is not None):
                conn = socket.socket(socket.AF_INET,
