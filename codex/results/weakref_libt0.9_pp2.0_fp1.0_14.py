import weakref

from tornado.options import options
from twisted.python import log
from twisted.internet import reactor, defer, task

from motor.mongo_replica_set_client import MotorReplicaSetClient
from motor.mongo_client import MotorClient, DEFAULT_MC_PORT, _MOTOR_CIMPORT
from motor.metaprogramming import (
    StringProperty, ReadOnlyProperty, DelegateMethod)


class MotorConnection(object):
    """All MotorConnection methods except close() are implemented. Pass
    them through to the motor_client.MotorClient instance. See
    motor_client.py for details.
    """
    host = ReadOnlyProperty()
    port = ReadOnlyProperty()

    def __init__(self, host, port, io_loop=None):
        db = MotorClient(
            host=host,
            port=port,
            io_loop=io_loop,
            peer_discovery=False
        )
        self.delegate = db

    def __getattr__(self, name):
        if self.delegate:
            return getattr(
