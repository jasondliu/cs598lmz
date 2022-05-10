from lzma import LZMADecompressor
LZMADecompressor()
import chucknorris
from Bio import Entrez
from Bio import Medline
import os
import re
from pprint import pprint
import joblib
from google.cloud import storage
import pickle
def getMedline(mid):
    try:
        Entrez.email = "d.mittelman.ts@gmail.com" # Always tell NCBI who you are
        handle = Entrez.efetch(db="pubmed", id=mid, rettype="medline", retmode="text")
        records = list(Medline.parse(handle))
    except:
        print '    error in getMedline'
        return None
    return records

def parseAbstractByLine(line):
    abstract = []
    abstrct = []
    iabs=0
    while 1:
        if iabs==0 and 'AB  -' in line:
            abstrct.append(line[5:])
        elif iabs>0 and '   '==line[:3]: 
            abstrct.append(line[3:])
        elif iabs>0 and '   '
