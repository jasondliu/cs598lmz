import socket
import sys
import threading
import time

from scapy.all import rdpcap
from scapy.all import sendp
from scapy.all import sniff
from scapy.all import wrpcap
from twisted.internet import reactor
from twisted.internet import task
from twisted.internet.protocol import DatagramProtocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.endpoints import TCP4ServerEndpoint

from model import *
import config


# define logfile for model
model_log = io.open(config.MODEL_LOG, 'w')

# define logfile for eval
eval_log = io.open(config.EVAL_LOG, 'w')

# define logfile for eval
replay_log = io.open(config.REPLAY_LOG, 'w')


class State:
    def __init__(self, mode):
        self.mode = mode
        self.learn_iter = 0
        self.replay_iter = 0
        self.part_num = 0

