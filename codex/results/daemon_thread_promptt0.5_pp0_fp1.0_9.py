import threading
# Test threading daemon
#
# @author ykk
# @date Sep 2011
#
import yapc.interface as yapc
import yapc.output as output
import yapc.events.openflow as openflow
import yapc.events.sockcore as sockcore
import yapc.netstate.netstate as netstate
import yapc.netstate.ofswitch as ofswitch
import yapc.log.output as logger
import yapc.pyopenflow as pyopenflow
import yapc.forwarding.simple as simple
import yapc.forwarding.l2_learning as l2learn
import yapc.comm.openflow as ofcomm
import time
import yapc.util.parse as pu
import yapc.events.openflow as ofevents
import yapc.util.etheraddress as eaddr
import yapc.forwarding.static as static

class test(yapc.daemon):
    def __init__(self, server):
        ##Bind to OpenFlow server
        server.register_event_handler(ofevents.pktin
