from lzma import LZMADecompressor
LZMADecompressor.decompress()

#reading the text file
with open("/content/drive/My Drive/Colab Notebooks/Data/20_newsgroups/20_newsgroup_training.txt", "r") as f:
    lst = f.read().splitlines()
f.close()
#editing the text
lst = [lst[i].replace("<", "") for i in range(len(lst))]
lst = [lst[i].replace(">", "") for i in range(len(lst))]
lst = [lst[i].replace(".", "") for i in range(len(lst))]
lst = [lst[i].replace(",", "") for i in range(len(lst))]
lst = [lst[i].replace("!", "") for i in range(len(lst))]
lst = [lst[i].replace("?", "") for i in range(len(lst))]
#making the text lowercase
lst = [lst[i].lower() for i in range
