import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def main():
    #inputFile = open("data/1.txt", "r", encoding='utf-8')
    inputFile = open("data/2.txt", "r", encoding='utf-8')
    #inputFile = open("data/3.txt", "r", encoding='utf-8')
    #inputFile = open("data/4.txt", "r", encoding='utf-8')
    #inputFile = open("data/5.txt", "r", encoding='utf-8')
    #inputFile = open("data/6.txt", "r", encoding='utf-8')
    #inputFile = open("data/7.txt", "r", encoding='utf-8')
    #inputFile = open("data/8.txt", "r", encoding='utf-8')
    #inputFile = open("data/9.txt", "r", encoding='utf-8')
    #inputFile = open("data/10.txt", "r",
