import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE
from threading import Thread
from xml.etree import ElementTree

from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import RegionInfo
from boto.exception import EC2ResponseError
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from aws.models import (
    EC2Instance,
    EC2InstanceType,
    EC2Region,
    EC2Zone,
    S3Bucket,
    S3BucketItem,
)

from aws.utils import (
    get_ec2_connection,
    get_s3_connection,
    get_s3_bucket_items,
