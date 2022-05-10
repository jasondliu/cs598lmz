from lzma import LZMADecompressor
LZMADecompressor().decompress(requests.get('https://pastebin.com/raw/KsyNt8Q7', stream=True).raw).decode()

# (/) Import requests
# (/) Import lzma library
# (/) LZMADecompressor to undecompress the string 
```

And the flag is :
```
encryptCTF{Sh3_w3nt_h0m3}
```
# 10. Audio Logic 1
*Description :*
```
Flag format : encryptCTF{flag}
Hint : I wrote a piece of music, where I hid the flag within it. Please add any effects that help you find the flag in the file.
```

**File** : [audio.wav](audio.wav)

#### Solution :
Seems like a steganography problem, and also the hint.
So i used [Audacity](https://www.audacityteam.org/)] to open this file but i didn't find anything inside.
Then, i tried to notice the wave activity noticed any patters and i found this :

![picture
