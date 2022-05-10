import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

# def get_text(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         text = f.read()
#     return text

if __name__ == '__main__':
    text = get_text(filename='E:\\coding\\python\\NLP\\NLP_learning\\data\\text\\test.txt')
    print(text)
