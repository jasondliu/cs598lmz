import select
import threading

from six.moves import queue

from ryu.controller import event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.event import EventBase
from ryu.lib import hub


class EventOFPMsgBase(event.EventBase):
    """Base class for events corresponding to OFP messages.

    This class has a dictionary 'msg' which is an instance of
    ryu.ofproto.ofproto_v1_0_parser.OFPXXX class corresponding to
    the OFP message.
    """
    def __init__(self, msg):
        super(EventOFPMsgBase, self).__init__()
        self.msg = msg


class EventOFPStateChange(EventOFPMsgBase):
    """Event to notify a change of state of an OpenFlow connection.

    An OpenFlow switch is identified by its datapath_id.
    """
    def __init__(self, msg, datapath_id, prev_state, state):
        super(EventOFPStateChange, self).__
