import types
types.ClassType = type

from boto.ec2.autoscale import AutoScalingGroup, LaunchConfiguration, ScalingPolicy
from boto.ec2.autoscale.tag import Tag

import boto.ec2.elb as elb

import boto.ec2.cloudwatch as cloudwatch
import boto.utils

import time
import os
import sys
import random
import string
import re

import logging
import logging.config

from optparse import OptionParser

from ConfigParser import ConfigParser

import copy

from boto.ec2.autoscale.tag import Tag

import pdb

# TODO: have a user-configurable list of regions to use
# TODO: have a user-configurable list of instance types to use
# TODO: have a user-configurable list of AMIs to use
# TODO: have a way to specify the number of instances per instance type
# TODO: have a way to specify the number of instances per AMI


