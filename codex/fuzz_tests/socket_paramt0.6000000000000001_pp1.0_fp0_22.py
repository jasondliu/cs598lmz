import socket
socket.if_indextoname('2')

```

```
import numpy as np
import pcap
import dpkt

# read pcap file
pc = pcap.pcap('test.pcap')
pkt_count = 0
for timestamp, buf in pc:
    pkt_count += 1
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    http = dpkt.http.Request(tcp.data)
    print '%d: %s %s' % (pkt_count, http.uri, http.headers['user-agent'])
```

```
import dpkt
import socket
import pygeoip
import optparse
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
           
