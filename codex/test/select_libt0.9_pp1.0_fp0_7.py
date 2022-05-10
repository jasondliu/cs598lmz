import selectors;
sys.path.insert(0,"../../");

from conf.configuration import ConfigurationManager
from lib.receiverleader import ReceiverLeader;
from lib.sequenceleader import SequenceLeader;
from lib.senderfollowers import SenderFollower;
from lib.boundedbuffer import BoundedBuffer;
from utils.logs import Log;
from threading import Thread;
from threading import Lock;
import logging;
import time;

class Executor(object):

    def __init__(self,configuration):
        self.config=configuration;
        self.senders=['sender1','sender2','sender3'];
    
    def __createObjectAndInjectConfiguration(self,factory):
        new_obj=factory();
        new_obj.injectConfig(self.config);
        return new_obj;


    
    @Log(logName="execute",logLevel=logging.INFO)
    def execute(self):

        self.config.set("PROCESS_ID","10000");
