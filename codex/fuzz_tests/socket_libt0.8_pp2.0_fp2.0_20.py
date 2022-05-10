import socket, sys
import optparse
from random import randint
from scapy.all import *
from random import randint

def randTcp():
    return TCP(sport=randint(1025,65500), dport=80)

def randIp():
    return IP(src=RandIP('*.*.*.*'), dst=RandIP('*.*.*.*'))


def create_packet(syn,ack,fin):
    if syn and ack:
        tcp = randTcp()
        ip = randIp()
        ans = IP(dst=ip.src, src=ip.dst)/TCP(dport=tcp.sport,sport=tcp.dport,flags='SA',seq=tcp.ack,ack=tcp.seq+1)
        return ip, tcp, ans
    if ack:
        tcp = randTcp()
        ip = randIp()
        ans = IP(dst=ip.src, src=ip.dst)/TCP(dport=tcp.sport,sport=tcp.
