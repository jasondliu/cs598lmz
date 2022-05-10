import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\r\r" + sys.path[0])).start()

import sys, os, re
from download import download

data = download("http://www.pyinstaller.org/wiki/SupportedPackages").split("\n")

for a in data:
    i = a.find("href=\"") + len("href=\"")
    j = a.find("\">", i)

    link = a[i:j]
    if link.startswith("wiki/"):
        continue

    download(link)

    print link

raw_input()
