import sys, threading

def run():
    sys.argv = ['main.py', 'runserver', '0.0.0.0:8000']
    execute_from_command_line(sys.argv)

t = threading.Thread(target=run)
t.start()

import time
time.sleep(3)

import requests

response = requests.get('http://127.0.0.1:8000/')
print(response.text)

response = requests.post('http://127.0.0.1:8000/', data={'name': 'mike'})
print(response.text)
