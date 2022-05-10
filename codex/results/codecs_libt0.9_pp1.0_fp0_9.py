import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import sys
import os

paths = [r"C:\Users\eXue\Downloads\Grand Theft Auto V"]

for path in paths:
    for root, subFolders, files in os.walk(path):
        for file in files:
            fullpath = os.path.join(root, file)
            if fullpath[-3:] == ".xtbl":
                command = 'x64n/xtbl2xml.exe x64n/xtbl2xml_settings.ini "' + fullpath + '" ' + fullpath[:-4] + "xml"
                print fullpath
                os.system(command)
