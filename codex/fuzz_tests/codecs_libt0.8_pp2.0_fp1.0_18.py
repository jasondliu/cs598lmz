import codecs
codecs.open('chinese.txt',mode='w',encoding='utf-8')

print(codecs.open('chinese.txt',mode='r',encoding='utf-8').read())
