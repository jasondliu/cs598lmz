import codecs
# Test codecs.register_error function
import random
import dmac_module
import Wifi_module
import Ir_module
import time

#IP = '112.121.172.1'
IP = '192.168.200.5'
PORT = 4050
macs = [] #mac tuples
macs_old = []
def server_task():
    #get data from hezi

    if not macs == macs_old:
        macs.sort(key=lambda tup: tup[1])  # sort least traffic first
        macs_old = macs
        print("sorted")
        print(macs)
    else:
        print("same")

    try:
            wifi = Wifi_module.Wifi_class(process = u"WeChat")
            data = wifi.format_for_server(macs)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT))
            s.send(data)
            print("server success")
    except:
        print("server fail")

