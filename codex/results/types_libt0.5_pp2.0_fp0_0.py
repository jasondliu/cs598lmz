import types
types.ModuleType.__init__.__globals__['_'] = lambda s: s
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Bind DNS Server",
                 "tr": "Bind DNS Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/named",
                 args="-u named",
                 pidfile="/var/run/named/named.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/named/named.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/named/named.pid")
