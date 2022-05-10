import socket
import ssl
import sys
import time

default_scheme = "amqps"
default_port = 5671
default_user = "sunstone"
default_pass = "sunstone"
default_queue = "sunstone"
default_exchange = "sunstone"
default_vhost = "/"

default_timeout = 1

class Host:

    addr = None
    user = default_user
    passwd = default_pass
    scheme = default_scheme
    queue = default_queue
    exchange = default_exchange
    vhost = default_vhost

    def __init__(self, host, **kwargs):
        # Try to split a possible host:port combination
        if ":" in host:
            host_ip = host.split(":")[0]
            host_port = host.split(":")[1]

            # Try to parse host_port as an integer
            try:
                host_port = int(host_port)
            except ValueError:
                raise Exception("%s is not a valid port" % host_port)

           
