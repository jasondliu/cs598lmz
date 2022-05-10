import socket
socket.if_indextoname(13)
import requests
response = requests.get("http://136.144.201.240")
#print(response.text)

import json
ad = """
{"status":"New", "children":1, "other":{"abc":123, "def":234}}
"""
j = json.loads(ad)
for i in j.keys():
    print("%s: %s" % (i, j[i]))
print("\n")    
for i in j['other'].keys():
    print("%s: %s" % (i, j['other'][i]))

import requests
import json

f = 
