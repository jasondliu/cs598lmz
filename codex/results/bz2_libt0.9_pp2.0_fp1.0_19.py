import bz2
bz2_file = bz2.BZ2File(".\\data\\train_cleaned.ft.txt.bz2")
# for i in range(10):
#     print(bz2_file.readline().decode("utf-8").strip())
data = []
with bz2_file as f:
    for i in range(10):
        print(f.readline().decode("utf-8").strip())

text = bz2_file.read().decode("utf-8")
print(type(text))
print(len(text))

data = text.split("\n")
print(type(data))
print(len(data))
print(data[:5])

nltk_data_dir = "C:\\Users\\ryang\\AppData\\Roaming\\nltk_data\\"
# nltk.download("punkt", nltk_data_dir)
texts = [[word for word in sentence.split(" ")] for sentence in data]

path = "C:\\Users\\ryang\\Documents\\GitHub
