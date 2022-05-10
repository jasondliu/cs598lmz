from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# it was further protected by base64 
import base64
base64.b64decode(data).decode()

# and the string was protected by xor(xor(key, text) ^ key) => xor(key, xor(key, text))
# therefore we just need to xor the previously decoded string with the key

key = b'B' * len(data)

# and we get the flag
xor(key, data).decode()
```

###### Flag: `KosenCTF{tHe_1t3ra1_i5_c0mp13x_th0ugh_i_knoW_yOu_can_f1gure_it_out}`
