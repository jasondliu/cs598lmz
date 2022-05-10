import threading
# Test threading daemon.
#
# @author ykk
# @date Jan 2011
#
import yapc.interface as yapc
import yapc.comm.rawsocket as rawsocket
import yapc.output as output
import yapc.events.openflow as openflow

class daemon(yapc.daemon):
    def __init__(self, server, port, ofconn):
        """Initialize

        @param server server IP
        @param port server port
        @param ofconn OpenFlow connection
        """
        yapc.daemon.__init__(self, server, port)
        self.ofconn = ofconn

    def run(self):
        (conn, addr) = self.sock.accept()
        output.dbg("Received connection from "+addr[0]+":"+str(addr[1]),
                   self.__class__.__name__)
        self.ofconn.send(openflow.ofmsg.hello())
        self.ofconn.send(openflow.ofmsg.features_request())
        conn.close()
        self.sock
