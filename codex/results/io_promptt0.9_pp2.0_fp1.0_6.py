import io
# Test io.RawIOBase
fo = io.BytesIO()

print('File closed?', fo.closed)
print( 'Opening mode:', fo.mode )
 
fo.close()
print('File closed?', fo.closed)

print( 'Opening mode:', fo.mode )

print()
# Test io.BufferedIOBase
fo = io.StringIO()

print('File closed?', fo.closed)
print( 'Opening mode:', fo.mode )
 
fo.close()
print('File closed?', fo.closed)

print( 'Opening mode:', fo.mode )

print()
# Test io.TextIOBase
fo = io.StringIO()

print('File closed?', fo.closed)
print( 'Opening mode:', fo.mode )
 
fo.close()
print('File closed?', fo.closed)

print( 'Opening mode:', fo.mode )
