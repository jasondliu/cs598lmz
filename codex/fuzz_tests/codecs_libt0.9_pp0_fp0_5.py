import codecs
codecs.open("abc.txt", "w", "utf-8")
## same as below
import sys
sys.getfilesystemencoding()
import os
print(os.fsencode("abc.txt"))
print(os.fsencode("가나다.txt"))


#### codecs.open("abc.txt", "w", "utf-8") 코드에서 문제점
f = codecs.open("abc.txt", "w", "utf-8")
print(f)
for i in range(10):
    data = "%d번째 줄입니다." % i
    f.write(data)
f.close()

## sys.getfilesystemencoding()처리한 코드
f = open("abc.txt", "w", encoding=sys.getfilesystemencoding())
print(f)
for i in range(10):
    data = "%d번째 줄
