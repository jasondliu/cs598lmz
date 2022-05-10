import socket
# Test socket.if_indextoname()
import sys
import time

import dpkt
import dshell.plugins.decoder
from dshell.output.alertout import AlertOutput
from dshell.output.netflowout import NetflowOutput

from dshell.output.alertout import AlertOutput
from dshell.output.netflowout import NetflowOutput
from dshell.output.summaryout import SummaryOutput
from dshell.util import DshellUtil
from dshell.util import ignore_exception

class DshellDecoder(dshell.plugins.decoder.UDPDecoder):
    """
    """

    def __init__(self):
        super(DshellDecoder, self).__init__(
            name="netflow",
            description="decode Netflow v5",
            author="dev",
            bpf="udp",
            optiondict={
                "summary": {"help": "output a summary at the end of the run", "action": "store_true", "default": False},
                "alert": {"help": "output an alert for each flow", "action": "store_true", "
