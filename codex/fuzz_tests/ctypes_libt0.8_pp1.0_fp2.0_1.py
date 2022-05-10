import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import urllib
def download(url, num_retries=2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html

url = "https://raw.githubusercontent.com/salman122/Python-Learning/master/PythonLearningCode.py"
download(url)

import requests
url = "https://raw.githubusercontent.com/salman122/Python-Learning/master/PythonLearningCode.py"
r = requests.get(url)
r.headers
r.content
r.text

