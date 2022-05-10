from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)

# scapy
from scapy.all import Ether, IP, sendp

sendp(Ether()/IP(dst='10.0.0.1'))

# requests
import requests

response = requests.get('https://www.baidu.com')
response.status_code

# beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content)
soup.find_all('a')

# pycryptodome
from Crypto.Cipher import AES
aes = AES.new(b'0123456789abcdef', AES.MODE_ECB)
aes.encrypt(b'0123456789abcdef')

# pysocks
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, 'localhost', 1080)
socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# pymongo
from pymongo import MongoClient
