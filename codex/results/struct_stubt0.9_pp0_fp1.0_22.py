from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.error = ValueError
s.format = 'If'
try:
    print(s.pack(2.0, 3.0, 4.0))
except TypeError:
    pass

try:
    print(s.unpack('a'))
except s.error:
    pass

obj = CausingError()

# _pickle.Pickler.save_global(obj)
# _pickle.Pickler.save_global(obj.__dict__)
# _pickle.Pickler.save_global(obj.__reduce__())


# class XMLParser: ...
#
# xml.sax.handler.ContentHandler.endElementNS(('NS', 'Tag'), None)
# parser.parseString(b'<xml>data</xml>')
