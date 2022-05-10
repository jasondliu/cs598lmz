import socket
import sys
import requests
import json
import random
import protobuf_json
import argparse

# For making the timestamp
from datetime import datetime
from datetime import timedelta

# protobuf imports
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict

# Protobuf imports
from protobuf.payload_pb2 import *
from protobuf.message_pb2 import *
from protobuf.position_pb2 import *
from protobuf.key_pb2 import *
from protobuf.user_pb2 import *
from protobuf.vehicle_pb2 import *

# Read in CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--topic', dest='topic', action='store', default='user', help='The topic of the message')
parser.add_argument('--type', dest='type', action='store', default='create', help='The type of message to send.')
parser.add_argument('--userid', dest
