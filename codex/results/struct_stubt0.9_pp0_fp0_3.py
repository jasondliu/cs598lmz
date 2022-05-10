from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
#print s.format_map(page_format)

print page_format
first_page = open('data/page')
page_pix = first_page.read(page_format['page_len'])

print 'page_pix len: %s'%page_pix.encode('hex').length
#page = struct.unpack(page_format_desc,page_pix)
page_format_desc = 
print page_format_desc
page = Struct(page_format_desc).unpack(page_pix)


print 'page = ',page
#exit(0)
#

#print 'page_pix: %s'%page_pix.encode('hex')

#header_format = {'frame_id':'II00II00II00II00II00II', 'frame_pix':'ffffff00ffffff00ffffff00', 'frame_type':16, 'frame_length':64, 'frame_len':80, 'frame_num':96, 'frame_rate':112,
