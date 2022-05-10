import socket
# Test socket.if_indextoname()
 
# Import socket module
import socket
 
# Function to convert a string address
# to Ipv4 formatted address
def convertStrToIp4(address):
    # Separate address by . and save in a list
    addrList = address.split(".")
 
    # Make address format xxx.xxx.xxx.xxx
    while(len(addrList)<4):
        addrList.append("0")
 
    # Convert to bytes
    addrBytes = bytes(''.join(addrList), encoding='utf8')
    return addrBytes
 
# Function to print filter rules
def printFilterRules(list, size):
    print("\nFilter rules:")
    for i in range(0, size):
        print("{0:<25}".format(list[i]), end='')
        if(i%2==1):
            print("\n")
 
# Function to convert binary address
# to a string
def convertIp4ToStr(address):
    ipAddr = ".".join(str(i) for i in address)
