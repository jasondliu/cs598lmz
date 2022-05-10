import bz2
bz2.decompress(data) 
# b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
```

Pattern 을 get 하는 과정에서 Flag 와 같은 문자열이 나오면, Pattern = Flag 가 아니라 결론을 낼 수 있다.
(문자열은 특수 문자를 제외, 숫자만 있다고 가정한다.)
이
