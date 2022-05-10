import codecs
codecs.open("1.txt", encoding="utf-8")

with codecs.open("1.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip().replace("\ufeff", ""))

with codecs.open("1.txt", encoding="utf-8") as f:
    content = f.read()
print(content)
