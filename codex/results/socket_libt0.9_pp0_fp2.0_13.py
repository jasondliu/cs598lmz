import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
local_ip = subprocess.check_output(['hostname', '-I']).decode('UTF-8')
local_hostname = subprocess.check_output(['hostname']).decode('UTF-8')
local_host_name = local_hostname.strip()
local_ip_name = local_ip.strip()
#*********************************************************************************************************************************
#Create MQTT client and connect to localhost, i.e. the Raspberry Pi running
# this script and the MQTT library.
client = mqtt.Client()
client.connect(b'localhost', 1883)
#Send some test messages and wait a few seconds in between.
client.publish('room/temperature', b'Test2')
time.sleep(0.5)
client.publish('room/humidity', local_ip_name
