import socket
# Test socket.if_indextoname method
# - This test case assumes that interface index 2 exists.
#
import support
import os
import socket

category  = "network"
target_host = os.environ.get("TARGET_IP")
target_port = int(os.environ.get("TARGET_PORT"))
def listen_to_port(port):
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    soc.bind((target_host, port))
    soc.listen(5)
  except:
    raise support.TestWarning("Failed to listen on port %d" % port)
  else:
    soc.close()

for intf_idx in [1, 2]:
    if_name = socket.if_indextoname(intf_idx)
    listen_to_port(target_port)
