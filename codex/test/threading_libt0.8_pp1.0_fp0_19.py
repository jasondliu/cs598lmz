import threading
threading._DummyThread._Thread__stop = lambda x: 42

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from datetime import datetime
from time import time


