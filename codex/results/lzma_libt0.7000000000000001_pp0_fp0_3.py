import lzma
lzma_filename = "091_meta.json.xz"
with lzma.open(lzma_filename, 'rt', encoding="utf-8") as f:
    meta = json.load(f)
 
# データ数
count = meta["count"]
print(count)

# データのタイプ
datatype = meta["datatype"]
print(datatype)

# データの最初の日付
firstday = meta["firstday"]
print(firstday)

# データの最後の日付
lastday = meta["lastday"]
print(lastday)

# データの日数(ステップ数)
step = meta["step"]
print(step)

# データの説明
description = meta["description"]
print(description)

# グラフのタイトル
title = meta["title"]
print(title)

# グラフのy
