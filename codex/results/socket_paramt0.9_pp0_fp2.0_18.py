import socket
socket.if_indextoname(1)

#%%

def check_wifi(interface_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

check_wifi('WIFI')

#%%
import subprocess
wifi_device = 0
wifi_device = [x for x in subprocess.getoutput('lsblk').split('\n') if 'WIFI' in x][0].split(' ')[0]
wifi_device
print(subprocess.getoutput('sudo ifconfig %s up' % wifi_device))
print(subprocess.getoutput('iwconfig %s' % wifi_device))
print(subprocess.getoutput('sudo ifconfig %s down' % wifi_device))


