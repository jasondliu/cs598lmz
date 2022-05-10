import lzma
lzma.LZMADecompressor

import zlib
zlib.decompress
'''

import lzma

filename  = 'temp/data.zip'
fieldname = 'data'

def get_data():
	with lzma.open(filename, mode = 'rb') as f:
		data = f.read().decode('UTF-8').split('\r\n')[0]
		data = data.split(',')[1].encode()
		data = base64.b64decode(data)
		data = data.decode('UTF-8')
		data = json.loads(data)
		return data

def time_norm(t):
	t = time.strptime(t, '%Y-%m-%d %H:%M:%S %Z')
	t = time.mktime(t) - time.timezone
	return int(t)

db = get_data()

for site in db:
	c = db[site]
	c['be
