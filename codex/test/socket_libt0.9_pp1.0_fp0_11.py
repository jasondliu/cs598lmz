import socket

from beacon.ttypes import Location

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from genpy.beacon.ttypes import BeaconService

class BeaconHandler:
  def ping(self):
    print("ping()")
  
  def getLocation(self, id):
    print("getLocation(" + id + ")")
    return Location(id=id, latitude=1.01, longitude=2.02, altitude=3.03)

def run_server():

  host = "127.0.0.1"
  port = 6000

  handler = BeaconHandler()
  processor = BeaconService.Processor(handler)
  transport = TSocket.TServerSocket(host=host, port=port)
  tfactory = TTransport.TBufferedTransportFactory()
  pfactory = TBinaryProtocol.TBinaryProtocolFactory()
