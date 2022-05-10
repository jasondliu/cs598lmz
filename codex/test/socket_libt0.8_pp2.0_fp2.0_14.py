import socket
import sys
import os

def pingLocal(host, target):
    host = str(host)
    target = str(target)
    
    response = os.system("ping -c 1 "+target)

    if response == 0:
        print ("ping to", target, "OK") 
    else:
        print ("no response from", target)


def pingRemote(host, target):
    host = str(host)
    target = str(target)
    url = "http://"+host+"/ping.php?target="+target
    print(url)
    response = os.system("curl "+url)
    print(response)

def getInterfaces(host, interface):
    host = str(host)
    interface = str(interface)
    url = "http://"+host+"/ifconfig.php?interface="+interface

    #response = os.system("curl "+url)
    #print(response)

    response = requests.get(url) 
    data = response.text 
