import weakref

from etcd import EtcdKeyNotFound
from etcd import EtcdResult

from tendrl.commons import flows
from tendrl.commons import objects
from tendrl.commons.event import Event
from tendrl.commons.message import ExceptionMessage
from tendrl.commons.utils import etcd_utils
from tendrl.commons.utils import log_utils as logger
from tendrl.commons.utils import util


def get_cluster_id(node_id):
    cluster_id = None
    try:
        node = objects.NodeContext(
            node_id=node_id
        ).load()
        cluster_id = node.cluster_id
    except (etcd.EtcdKeyNotFound, KeyError):
        pass
    return cluster_id


def get_cluster_name(cluster_id):
    cluster_name = None
