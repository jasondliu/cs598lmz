import threading
threading.currentThread().setName("py4j.GatewayServer")

import sys
import re
import subprocess
import os
import time

from py4j.java_gateway import launch_gateway, JavaObject, CallbackServerParameters
from py4j.java_gateway import java_import, JavaGateway, GatewayParameters
from py4j.java_gateway import get_field, set_field
from py4j.java_collections import JavaObject
from py4j.java_gateway import Py4JNetworkError

from cluster import ClusterManager
from cli import AddResource
from novacluster import NovaCluster
from awscluster import AWSTestCluster
from cindercluster import CinderCluster
from ec2cluster import EC2TestCluster
from ec2cluster import EC2TestClusterWithCinder
from valetcluster import ValetCluster
from testconfig import task_defaults
from util import sync_calls, async_calls

logger = logging.getLogger(__name__)

