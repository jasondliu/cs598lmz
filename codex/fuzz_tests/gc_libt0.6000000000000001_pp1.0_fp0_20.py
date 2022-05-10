import gc, weakref
from cStringIO import StringIO
from cPickle import dumps, loads
from threading import Thread, Event
from functools import wraps
from contextlib import contextmanager

from nose.tools import assert_equal, assert_false
from nose.tools import assert_raises, assert_true, assert_is_none
from nose.tools import assert_is_instance
from nose.tools import assert_in
from nose.tools import assert_greater_equal

from celery.utils import uuid
from celery.utils.serialization import pickle
from celery.backends import default_backend
from celery.backends.base import DisabledBackend
from celery.backends.amqp import AMQPBackend
from celery.backends.cache import CacheBackend
from celery.backends.dummy import DummyBackend
from celery.backends.mongodb import MongoBackend
from celery.backends.redis import RedisBackend
from celery.backends.riak import RiakBackend
from celery.backends.cassandra import Cassandra
