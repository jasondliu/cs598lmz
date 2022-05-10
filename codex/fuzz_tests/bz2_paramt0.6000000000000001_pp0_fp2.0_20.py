from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("dumps/enwiki-latest-pages-articles.xml.bz2", "rb").read())
import bz2
bz2.BZ2File("dumps/enwiki-latest-pages-articles.xml.bz2").read()

import pandas as pd

#df = pd.read_csv("dumps/enwiki-latest-pages-articles.xml.bz2", sep="\t")
df = pd.read_csv("dumps/enwiki-latest-pages-articles.xml", skiprows=[0,1], sep="\t")

df.head()

#df = pd.read_csv("dumps/enwiki-latest-pages-articles.xml", skiprows=1, sep="\t")
#df.head()

#pd.read_csv("dumps/enwiki-latest-pages-articles.xml", sep="\t")

#import xml.etree.ElementTree as ET
#tree = ET.parse("dumps/enwiki-latest-pages-articles.xml")

