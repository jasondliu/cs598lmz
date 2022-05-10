import socket
socket.if_indextoname(3)

# Get interface details
import netifaces
#netifaces.interfaces()
#netifaces.ifaddresses('en0')
#netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']

# Get system mac address
import uuid
#hex(uuid.getnode())

# Get system name
import platform
platform.node()

# Get CPU temperature
import os
#os.popen('vcgencmd measure_temp').readline()

# Get IP address
import socket
#socket.gethostbyname(socket.gethostname())

# Get CPU usage
import psutil
#psutil.cpu_percent(interval=1)

# Get GPU usage (Raspberry Pi)
import os
#os.popen("/opt/vc/bin/vcgencmd measure_volts core").read().replace("volt=", "").replace("V\n", "")

