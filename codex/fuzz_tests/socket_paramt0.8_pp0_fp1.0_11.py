import socket
socket.if_indextoname('3')

import netifaces

for i in netifaces.interfaces():
    print(i)

netifaces.ifaddresses('en0')

netifaces.ifaddresses('en0')[netifaces.AF_LINK]

netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']

netifaces.ifaddresses('p2p0')

netifaces.ifaddresses('p2p0')[netifaces.AF_LINK]

netifaces.ifaddresses('p2p0')[netifaces.AF_LINK][0]['addr']

netifaces.ifaddresses('awdl0')

netifaces.ifaddresses('awdl0')[netifaces.AF_LINK]

netifaces.ifaddresses('awdl0')[netifaces.AF_LINK][0]

netifaces.ifaddresses('awdl0')[netifaces.AF_LINK][0]['addr']


