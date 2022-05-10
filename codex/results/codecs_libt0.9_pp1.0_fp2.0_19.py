import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

global_delay = [0,0]
global_latency = [0,0]
global_jitter = [0,0]
global_lost = []

'''
name = ['192.168.0.103', '192.168.0.102']
global_delay = {
    '192.168.0.103': [],
    '192.168.0.102': []
}'''

def calculate_delay(pkt):
    if ("ICMP" in protocol) or ("TCP" in protocol) or ("UDP" in protocol):
        pkt_src = pkt[0][1].src
        pkt_dst = pkt[0][1].dst
        pkt_time = pkt[0][1].time
        return pkt_src,pkt_dst,pkt_time
    else:
        protocol = pkt[0][1].proto
        print("Sorry! We cannot calculate delay of
