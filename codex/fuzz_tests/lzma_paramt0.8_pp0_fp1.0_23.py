from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

#pip freeze > requirements.txt
#pip install -r requirements.txt

#Регулярные выражения
#Функция, возвращающая список из форм слова, которые начинаются с гласной буквы

def stress(word):
    res = []
    for i in range(len(word)
