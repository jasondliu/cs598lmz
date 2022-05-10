import mmap
# Test mmap.mmap
# https://docs.python.org/2/library/mmap.html
#
# Create a buffer
#
# @author ykk
# @date Feb 2011
#
import yapc.interface as yapc
import yapc.comm.udp as udp
import yapc.log.output as output
import yapc.local.core as local
import yapc.pyopenflow as pyof
import yapc.events.openflow as ofevents
import yapc.events.openflow.ofmsg as ofmsg
import yapc.events.openflow.ofp_event as ofp_event
import yapc.netstate.net as netstate
import yapc.netstate.ofswitch as ofswitch
import yapc.openflow.message as ofmsg
import yapc.util.parse as pu
import yapc.forwarding.openflow.ofswitch as ofswitch
import yapc.forwarding.openflow.ofrecv as ofrecv
import yapc.forwarding.openflow.ofserver as ofserver
import y
