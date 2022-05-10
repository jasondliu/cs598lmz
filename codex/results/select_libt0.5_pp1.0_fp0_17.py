import select
import socket
import sys
import threading
import time

import boto.ec2
import boto.ec2.autoscale
import boto.ec2.elb
import boto.ec2.elb.healthcheck
import boto.exception
import boto.route53
import boto.route53.record
import boto.route53.zone
import boto.utils
import boto.vpc
import boto.vpc.networkinterface

import config
import util
import util.ec2
import util.elb
import util.route53

log = logging.getLogger(__name__)

class Route53Error(Exception):
    pass

class Route53RecordSet(object):
    def __init__(self, zone, name, type, ttl=60):
        self.zone = zone
        self.name = name
        self.type = type
        self.ttl = ttl
        self.old_record = None

    @property
    def fqdn(self):
        return '%s.%s' % (
