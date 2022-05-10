import ctypes
ctypes.cast(pointer, ctypes.py_object).value

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
# Create a cipher object using the random secret
cipher = AES.new(key)
decoded = cipher.decrypt(encrypted).decode('utf-8')
print('Decrypted: ', decoded)

# Split on the comma
data = decoded.split(',')

# Put the data into a dictionary
d = {'ticker': data[0],
     'date': data[1],
     'closing price': data[2]
     }
print(d)
