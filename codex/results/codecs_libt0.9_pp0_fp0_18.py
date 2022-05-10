import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime, time
import re

print "Loading Events..."

with open('c:\python27\ath.txt', 'rb') as csvfile:
    #with open('c:\python27\EventsT.txt', 'rb') as csvfile:
    athreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    Events = list()
    count = 0
    for row in athreader:
        date = row[0].split('/')
        newdate = date[2]+'-'+date[0]+'-'+date[1]
        row[0] = newdate
        Events.append(row)
    
print "Loading Start List..."

with open('c:\python27\start.txt', 'rb') as csvfile:
