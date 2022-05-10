import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

with open(r'C:\Users\MADHUKAR\Desktop\sravya.txt', 'r') as file:
    data = file.read()
    data = data.replace('\n', ' ')
    print(data)
    words = data.split()
    print(words)
    print(len(words))
    print(len(data))
    print(words.count('vizianagaram'))
    print(words.index('vizianagaram'))
    with open('sravya_out.txt', 'w') as f:
        for word in words:
            print(word, file=f)
