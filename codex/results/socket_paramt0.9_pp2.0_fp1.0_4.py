import socket
socket.if_indextoname()

"""

class hackDB(object):
    """Class for communicating with a HackDB server"""

    def __init__(self, hackdb_host="141.212.11.199", hackdb_port=9999, uuid="NO_UUID_GIVEN"):
        self.hackdb_host = hackdb_host
        self.hackdb_port = hackdb_port
        self.uuid = str(uuid)
        #self.setup(hackdb_host, hackdb_port, uuid)

    #def setup(self, host="141.212.11.199", port=9999, uuid="NO_UUID_GIVEN"):
    #    self.hackdb_host = str(host)
    #    self.hackdb_port = int(port)
    #    self.uuid = uuid
    
    def send(self, msg, tag=None):
        """Sends a message to the host"""
        if tag is None:
            payload = self.uuid + " " + str(msg)
        else:
            payload
