import codecs
# Test codecs.register_error('myreplacer', __replacer)
def __replacer(unichr):
    return ""
codecs.register_error('myreplacer', __replacer)
def my_encoder(x):
    return x.decode('utf_32').encode('utf-8', 'myreplacer')
def my_decoder(x):
    return x.decode('cp-1252', 'replace').encode('utf_32')

def _fill(s, length):
	s = s[0:length]
	sl = len(s)
	rest = length-sl
	for x in range(0, rest):
		s = s + " "
	return s

def createTabloTxt(
    dir_in,table_name,table_type,
    columns,columns_types,columns_sizes_mn,columns_sizes_mx,columns_fillers,
    top_line=None
    ):
    file_name = '%s\%s.txt' % (dir_in, table_name)
   
