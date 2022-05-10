import socket
socket.if_indextoname(2)

# 方法二：使用第三方库
import netifaces
netifaces.ifaddresses('eth1')
netifaces.ifaddresses('eth1')[netifaces.AF_LINK][0]['addr']

# 方法三：使用系统命令
import os
os.popen('ipconfig').read()

# 方法四：使用Popen执行系统命令
import subprocess
p = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, shell=True)
p.stdout.read()

# 方法五：使用psutil
import psutil
psutil.net_if_addrs()

# 方法六：使用psutil
import uuid
uuid.getnode()
