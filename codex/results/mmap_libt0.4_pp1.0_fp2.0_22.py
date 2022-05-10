import mmap
import re
import sys
import time
import traceback
import tty
import termios

import boto3
import botocore

from . import util
from . import constants
from . import __version__

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.NullHandler())

# Set up boto3
boto3.set_stream_logger(name='botocore', level=logging.WARNING)

# Set up AWS session
aws_session = boto3.Session()

# Set up AWS clients
ec2 = aws_session.client('ec2')
ecs = aws_session.client('ecs')
elb = aws_session.client('elbv2')
iam = aws_session.client('iam')
s3 = aws_session.client('s3')

# Set up AWS resource
ec2_resource = aws_session.resource('ec2')
ecs_resource = aws_
