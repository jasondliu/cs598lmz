import socket
socket.if_indextoname('0')

import subprocess
output = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
output.stdout.decode('utf-8').split()

import json
s = open('songs.json','r').read().strip().split('\n')[0]
#print(s)
x = json.loads(s)
#print(x)

# I hate myself for doing this, but at level 5 I got it to work!!!
x = x.replace('u\'', '\'')
x = x.replace('\'', '\"')
x = x.replace('None', 'null')
x = re.sub(r' ([a-zA-Z0-9]):', r' "\1":', x)
x = re.sub(r'(\{|\,)\:([a-zA-Z0-9])', r'\1"\2', x)
x = re.sub(r'False', r'false', x)
x = re.sub(r'True', r'true', x)

