import socket
import sys
from optparse import OptionParser

from motmot.realtime_image_analysis.rtgraph import (
    RTGraph,
    RTFigureCanvas,
    RealtimeFigure,
    )

from motmot.realtime_image_analysis.incoming_request_handler import (
    IncomingRequestHandler,
    )

class ListenerThreadBase(threading.Thread):
    def __init__(self,owner,source_from_main=None):
        super(self.__class__,self).__init__()
        self.owner = owner
        if source_from_main is None:
            # first assert that the main window has a single figure
            if len(self.owner.figures)!=1:
                raise RuntimeError('Must have one figure for listener thread')

            # if this switch is on, then the listener thread uses
            # the same figure as the main thread, otherwise it uses its
            # own copy
            self.source_from_main = True
        else:
            self.source_from_main = source_from_main

