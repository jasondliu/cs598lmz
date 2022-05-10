import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# 讀取 CSV 檔內容
data = []
with open('./data/example.csv', 'r', encoding='utf-8') as f:
  for line in csv.reader(f):
    data.append(line)

# 轉置矩陣
data = list(map(list, zip(*data)))

# 印出結果
print(data)

# 寫入 CSV 檔
with open('./data/example2.csv', 'w', encoding='utf-8', newline='') as f:
  w = csv.writer(f)
  for rec in data:
    w.writerow(rec)

# 讀取 CSV 檔案內容
with open('./data/example2.csv', newline='', encoding='utf-8') as csvfile:

