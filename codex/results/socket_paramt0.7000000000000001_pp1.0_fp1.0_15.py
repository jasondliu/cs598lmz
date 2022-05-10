import socket
socket.if_indextoname(7)

from subprocess import call
import netifaces as ni
ni.ifaddresses('lo')
ni.ifaddresses('eth0')
ni.ifaddresses('wlan0')

import netifaces as ni
ni.interfaces()
ni.ifaddresses('lo')
ni.ifaddresses('eth0')
ni.ifaddresses('wlan0')

import netifaces as ni
ni.interfaces()
ni.ifaddresses('eth0')

import netifaces as ni
ni.interfaces()
ni.ifaddresses('eth0')
ni.ifaddresses('wlan0')

import netifaces as ni
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

import netifaces as ni
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print ip

import netifaces as ni
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print ip

