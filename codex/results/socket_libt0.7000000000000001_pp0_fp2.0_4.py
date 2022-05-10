import socket
import netifaces
#from netifaces import *

# -- General stuff ------------------------------------------------------------

def get_plug_internal_ip():
    """
    Finds the internal IP of the smart plug.
    """
    # TODO: make this work on platforms other than Raspbian
    dirmac = "/sys/class/net/eth0/address"
    with open(dirmac, "r") as f:
        mac = f.read()
    ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    return ip, mac

def get_plug_lan_ip():
    """
    Finds the LAN IP of the smart plug.
    """
    # TODO: make this work on platforms other than Raspbian
    dirmac = "/sys/class/net/eth0/address"
    with open(dirmac, "r") as f:
        mac = f.read()
    gws = netifaces.gateways()
    gw = gws['default'][netif
