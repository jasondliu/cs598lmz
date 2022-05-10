import codecs
codecs.register_error("surrogatepass", codecs.surrogatepass_handler)
'+5678901234567890'
'✔✔✔'
u"a\u0394"
u"a\u0394".encode('utf-16')
'\ud809\udcb3'
'\ud809\udcb3'.encode("utf-8")
'abcdef\u0394'
'abcdef\u0394'.encode("utf-8")
'\ud809\udcb3'.decode("utf-16")
'✔✔✔'.decode("utf-16")
'✔✔✔'.decode("utf-8")
'✔✔✔'.decode("utf-8", "surrogatepass")
'✔✔✔'.decode("utf-8", "replace")
 
u"abcdef\u0394"
u"abcdef\u0394".encode("utf-8")
u"abcdef\u0394".encode("utf-16")
 
u"a
