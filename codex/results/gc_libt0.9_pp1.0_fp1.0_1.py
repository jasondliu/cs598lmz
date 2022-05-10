import gc, weakref, copy
import sys       # self.flush

from _utils import *   # logging, LOG, JsonEncoder


#  Time
import datetime as DT

#  ================================================================================================
class pubsub(object):

  def __init__(self, url="amqp://guest:guest@localhost:5672/%2F", exchange="default_exchange", *args, **kwargs):
    super(pubsub,self).__init__( *args, **kwargs )
    self._param = {
        'url':url,
        'exchange':exchange,
        'type':'fanout',
        'durable':True,
        'auto_delete':False,
        'exclusive':False,
        }
    self._param.update( kwargs )
    self._exchange = exchange
    self._outstanding = []
    self._connection = None
    self._channel = None

    self._connection = pika.BlockingConnection(pika.URLParameters(url))
    self._channel = self._connection.channel()
    self._
