from lzma import LZMADecompressor
LZMADecompressor().decompress(b'Hello')

s = '가나다라마'
#utf-8
len(s.encode('UTF-8')), len(s.encode('UTF-16'))

def word_counter(file_name, word):
    word_count = 0
    with open(file_name) as f:
        for line in f:
            if line.lower().find(word) >= 0:
                word_count += 1
    return word_count
word_counter('DataScience/data/milkandbread.txt', 'the')

def is_year(year):
    if not isinstance(year, int):
        return False
    
    if year % 4 == 0:
        return True
    else:
        return False

print(is_year(2020))
print(is_year(2001))
print(is_year('2020'))

def OddEven(num):
    if isinstance(num, int) and num % 2 == 0:
        print("Even")
        return True
