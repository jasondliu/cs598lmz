import codecs
codecs.register_error('strict', codecs.ignore_errors)
#import subprocess
#from subprocess import STDOUT
import time
import string

def unix2dos(fname):
    tempname=fname+'.tmp'
    infile=open(fname,'rb')
    outfile=open(tempname,'wb')
    for s in infile:
        outfile.write(s.replace(b'\n', b'\r\n'))
    infile.close()
    outfile.close()
    os.remove(fname)
    os.rename(tempname,fname)

def dos2unix(fname):
    tempname=fname+'.tmp'
    infile=open(fname,'rb')
    outfile=open(tempname,'wb')
    for s in infile:
        outfile.write(s.replace(b'\r\n', b'\n'))
    infile.close()
    outfile.close()
    os.remove(fname)
    os.rename(tempname,f
