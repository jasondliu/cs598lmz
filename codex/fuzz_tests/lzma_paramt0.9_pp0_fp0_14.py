from lzma import LZMADecompressor
LZMADecompressor().decompress(d)

# more robust size extraction and decompression

def compressed_size_and_data(d):
    s = d[-4:]
    for byte in s:
        n = byte ^ 0xFF
        if n > 0x80:
            return False,None,None
    sz = struct.unpack(">I", d[-4:])[0]
    return True, sz,d[:-4]
    
ok, sz, d = compressed_size_and_data(data)

if ok:
    print(sz)
    LZMADecompressor().decompress(d)
else:
    print('invalid data')
 
```

## decompression in go
```golang

package main

import (
	"fmt"
	"github.com/ulikunitz/xz/lzma"
	"os"
)

func main() {
	var d []byte

	f, err := os.Open("./7.oceania.lz
