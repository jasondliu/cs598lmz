import _struct

# dpkt.ethernet
# dpkt.ieee80211
# dpkt.ip
# dpkt.ip6
# dpkt.loopback
# dpkt.pcap
# dpkt.pcapng
# dpkt.ppp
# dpkt.radiotap
# dpkt.raw
# dpkt.stp
# dpkt.tcp
# dpkt.udp

def decode_tcp(data):
    try:
        return dpkt.tcp.TCP(data)
    except:
        return None

def decode_udp(data):
    try:
        return dpkt.udp.UDP(data)
    except:
        return None

def decode_ip(data):
    try:
        return dpkt.ip.IP(data)
    except:
        return None

def decode_ip6(data):
    try:
        return dpkt.ip6.IP6(data)
    except:
        return None


