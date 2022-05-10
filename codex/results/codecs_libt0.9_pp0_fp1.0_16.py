import codecs
codecs.open(filepath, "r","sjis").read()

#2.シフトJISであるテキストファイルを読み込みたい
with open(filepath, encoding="sjis") as f:
    print(f.readline())


#3. シフトJISであるテキストファイルを書き込みたい
#
#ioモジュールを使用する。
