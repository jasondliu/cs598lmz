import socket

from kombu import BrokerConnection, Exchange, Queue, Consumer, Connection

from mq.proxy import RPC_EXCHANGE_NAME
from mq.utils import connection
from mq.utils.threads import PeriodicTask
from mq.utils.zmq_proxy import ZmqProxy

log = logging.getLogger(__name__)

DEFAULT_CONSUME_TIMEOUT = 1


def get_broker_conn():
    return BrokerConnection(hostname=settings.MQ_HOST,
                            userid=settings.MQ_USER,
                            password=settings.MQ_PASS,
                            virtual_host=settings.MQ_VHOST)


def message_to_dict(msg):
    return {key: value for key, value in vars(msg).iteritems()
            if not key.startswith('_')}


class BaseConsumer(object):

    def __init__(self, queues=None, connection=None, exchange=None,
                 prefetch_count=None, timeout=DEFAULT_CONSUME_
