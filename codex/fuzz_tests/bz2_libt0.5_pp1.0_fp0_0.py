import bz2
bz2_file = bz2.BZ2File('example.bz2')

# データを読む
data = bz2_file.read()
data

# ファイルを閉じる
bz2_file.close()

# ------------------------------------
# bz2 ファイルを開く
# ------------------------------------
import bz2
bz2_file = bz2.BZ2File('example.bz2')

# データを読む
for line in bz2_file:
    print(line)

# ファイルを閉じる
bz2_file.close()

# ------------------------------------
# bz2 ファイルを開く
# ------------------------------------
import bz2
bz2_file = bz2.BZ2File('example.bz2')

# データを読む
data = bz2_file.readlines()
data

# ファイルを閉
