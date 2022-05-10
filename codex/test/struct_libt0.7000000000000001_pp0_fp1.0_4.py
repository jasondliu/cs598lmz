import _struct
import sys

print(sys.version)
print(sys.executable)

def convert(s):
    i=0
    x=0
    while i<len(s):
        c=s[i]
        if c>='0' and c<='9':
            x=x*16+int(c,16)
        i=i+1
    return x

def convert_hex(s):
    i=0
    x=0
    while i<len(s):
        c=s[i]
        if c>='0' and c<='9':
            x=x*16+int(c,16)
        i=i+1
    return x

def convert_str(s):
    i=0
    x=0
    while i<len(s):
        c=s[i]
        if c>='0' and c<='9':
            x=x*16+int(c,16)
        i=i+1
    return x

