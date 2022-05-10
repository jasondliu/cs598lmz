import weakref
from threading import Timer
from mininet.log import *

def get_topo(name):
    """
    Get the topology for a specified name.

    :param name: The name of the topology to create"""
    topos = get_topos()
    if name not in topos:
        raise KeyError('Unknown topology: %s; available topologies are: %s'
                       % ( name, ', '.join( topos.keys() ) ) )
    return topos[name]()

def get_topos():
    """
    Return a dict of available Topologies (without creating them)
    """
    topos = {}
    for name, value in globals().items():
        if name in globals() and isinstance( value, type ) and \
                issubclass( value, Topo ) and value != Topo:
            topos[ name ] = value
    return topos

class IPAddr(object):
    "A simple IPv4 IP address class."

    num = 0

