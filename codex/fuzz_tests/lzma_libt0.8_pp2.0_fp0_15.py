import lzma
lzma.decompress(open(filename, 'rb').read()).decode()
# pdftotext with -enc UTF-8 option

# utf-8
with open(filename, 'rb') as f:
    text = f.read()

# latin-1
with open(filename, 'rb') as f1:
    text = f1.read().decode('latin-1')

# try: utf-8
# except: latin-1
try:
    with open(filename, 'rb') as f:
        text = f.read().decode('utf-8')
except:
    with open(filename, 'rb') as f1:
        text = f1.read().decode('latin-1')

# try: utf-8
# except: latin-1
# else: ascii
try:
    with open(filename, 'rb') as f:
        text = f.read().decode('utf-8')
except:
    with open(filename, 'rb') as f1:
        try:
