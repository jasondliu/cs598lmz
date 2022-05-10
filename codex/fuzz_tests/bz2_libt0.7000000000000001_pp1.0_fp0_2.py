import bz2
bz2_file = bz2.BZ2File('/home/kyohei/pydata-book/ch02/sample.json.bz2')
data = bz2_file.read()
bz2_file.close()
data

## 9.9 文字列とバイト列
# Unicode文字列からバイト列へ変換
s = 'pýtĥöñ\fis\tawesome\r\n'
s

#バイト列に変換すると'ascii'エンコーディングではエラーになる
remainder = b'a'
remainder.decode('ascii')

# 'utf-8'でエンコードするとエラーにならない
remainder = b'a'
remainder.decode('utf-8')

# 一部分だけエラーになる
b = s.encode('utf
