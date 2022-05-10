import sys, threading

def run():
    while 1:
        ip = raw_input('Enter IP to scan: ').split('.')
        if (len(ip) == 4):
            break
    if ip[0] == '192' and ip[1] == '168':
        print "scanning local area network"
        for i in range(1, 255):
            for j in range(1, 255):
                sys.stdout.write('.')
                sys.stdout.flush()
                ip[2] = str(i)
                ip[3] = str(j)
                addr = '.'.join(ip)
                t = threading.Thread(target=pinger, args=(addr,))
                t.start()
                t.join()
        print "scan complete"
    else:
        print "scanning internet"
        for i in range(1, 255):
            sys.stdout.write('.')
            sys.stdout.flush()
            ip[3] = str(i)
            addr = '.'.join(ip)
            t = threading.Thread(target
