import select
# Test select.select
select.select([],[],[],0.0)
# End test
from PIL import Image
from PIL import ImageFile
import cStringIO
import threading
import time
from Queue import Queue
from Queue import Empty
from Queue import Full
from threading import Thread
from time import sleep
from time import time
import sys
import socket
import os
import fcntl
import errno
from socket import error as socket_error
from urlparse import urlparse
from httplib import HTTPConnection
import traceback
import random
from random import randint
import hashlib
import base64

from boto.ec2.blockdevicemapping import BlockDeviceMapping, BlockDeviceType
from boto.ec2.blockdevicemapping import EBSBlockDeviceType
from boto.vpc import VPCConnection
from boto.ec2.networkinterface import NetworkInterfaceCollection
from boto.ec2.networkinterface import NetworkInterfaceSpecification
from boto.ec2.networkinterface import PrivateIPAddress
