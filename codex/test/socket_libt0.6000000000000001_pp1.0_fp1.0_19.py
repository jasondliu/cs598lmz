import socket
import codecs
import os

#socket.setdefaulttimeout(5)

def find_url(url):
    #print(url)
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        html = html.decode('utf-8')
    except:
        return None
    return html

def find_url_list(url):
    html = find_url(url)
    if html == None:
        return None
    #print(html)
    soup = BeautifulSoup(html, features="html.parser")
    #print(soup)
    #soup = soup.find('div', {'class':'tpc_content'})
    #print(soup)
    #print(soup.find_all('a'))
    url_list = []
