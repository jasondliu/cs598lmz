import codecs
codecs.register_error("msgpack_utf8", codecs.lookup_error("utf8"))
def __get_mbuf_length(buf):
	nLen = 0
	try:
		nLen = buf.split("\t")[1]
	except Exception, e:
		pass
	return int(nLen)

def __get_lbuf_length(buf):
	nLen = 0
	try:
		nLen = buf.split("\t")[1]
	except Exception, e:
		pass
	return int(nLen) 

class read_mtime_file(mr.Step):
	def __init__(self):
		mr.Step.__init__(self)
	
	def mapper(self, input_path, input_file):
		for line in input_file:
			if len(line) < 6:
				continue
			try:
				time_stamp = long(line.strip())
				yield "mt", time_stamp
			
