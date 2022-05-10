import codecs
codecs.open("kjvdat.txt", "r", "ascii")

f = open("kjvdat.txt", 'r')

l = f.readlines()

dict = {}

for x in l:
    x = x.split(":")
    if x[0] in dict:
        dict[x[0]].append(x[1])
    else:
        dict[x[0]] = [x[1]]

f.close()

print(dict)
