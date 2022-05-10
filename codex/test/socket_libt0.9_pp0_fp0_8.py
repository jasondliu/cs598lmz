import socket

#Check args
if len(sys.argv) < 2 :
    print("usage: python tcp-scan-v2.py ip-start ip-end port-number")
    print("Example: python tcp-scan-v2.py 192.168.5.0 192.168.5.100 135")
    sys.exit(1)


#Get args (ip-start, ip-end, port-number)
ipStart = sys.argv[1]
ipEnd = sys.argv[2]
portNumber = sys.argv[3]

#Creo la lista con gli IP da controllare
ipList = []
