import codecs
codecs.open

f=codecs.open('c:\\tmp\\text.txt','r', 'utf-8')
f.read()

f.seek(0)
f.read()
f.close()
f=codecs.open('c:\\tmp\\text.txt','r', 'utf-8-sig')
f.read()
f.close()
