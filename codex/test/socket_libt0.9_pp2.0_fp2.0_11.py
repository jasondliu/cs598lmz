import socket
from time import sleep
import cPickle as pickle
from threading import Thread, RLock, Event

from rmq_params import connection_params, queue_name


try:
    from redis import StrictRedis

    REDIS_READY = True
except ImportError:
    REDIS_READY = False


def get_multi():
    if REDIS_READY:
        redis = StrictRedis(db=1)
        return redis.pipeline()
    return None


def prep_redis_counter(redis, counter_name):
    return redis.incr('counter:%s' % counter_name, 0)


def logger(*args):
    # print(' '.join(str(a) for a in args))
    return


class RMQListener(object):
    def __init__(self, mailbox, nb=True, fname=None, timeout=1.0):
        self.mailbox = mailbox
        self.nb = nb
        self.timeout = timeout
