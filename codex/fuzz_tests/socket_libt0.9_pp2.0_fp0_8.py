import socket
import urllib.request
from bs4 import BeautifulSoup
data=socket.socket(socket.AF_INET, socket.SOk_STREAM)
data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
data.connect(('localhost',8080))
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0"}
header={"#wsgi.url_scheme":"http"}
#print(issubclass(dict,list))
rs='GET / HTTP/1.1\r\n'
rs+='Host: localhost:8080\r\n'
rs+='Connection: close\r\n'
rs+='\r\n'
data.send(bytes(rs,'UTF-8'))

topage='''
<html>
<head>
    <title>Architecture </title>
    <link rel="stylesheet" href="https://stackpath
