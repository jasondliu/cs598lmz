import bz2
bz2.BZ2Compressor()

c = cStringIO.StringIO()
chunk = 'this should get compressed 5'
while 1:
    c.write(chunk)
    print(len(chunk))
    chunk = c.getvalue()
    break

c.close()

#cStringIO and StringIO are useless as just generators.
#you have to hold the entire file in memory.
c = cStringIO.StringIO()
c.write('oi there im a cstringio strin')
c.write('g i like to be compressed, it is naturally my calling')
c.write(' to be compressed')

print(c.readlines())

#ok, but, in a holding pen?!

c = cStringIO.StringIO()
c.write('oi there im a cstringio strin')
c.write('g i like to be compressed, it is naturally my calling')
c.write(' to be compressed')

print(c.readlines())

#ok, but you can't write if your cursor is near the end of the file!

c
