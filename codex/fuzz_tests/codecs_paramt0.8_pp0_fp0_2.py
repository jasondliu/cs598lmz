import codecs
codecs.register_error('ignore', codecs.replace_errors)

FILE_PATH = 'E:/NLP_Project/Code/keyword'
SYS_PATH = 'E:/NLP_Project/Code/'
INPUT_DIR = 'input_data/'
OUTPUT_DIR = 'out_data/'

def en_segmentation(text):
    '''
    英文分词
    '''
    try:
        en_seg = nltk.tokenize.word_tokenize(text)
        return en_seg
    except Exception as e:
        print('en', e)
        return []


def cn_segmentation(text):
    '''
    中文分词
    '''
    try:
        cn_seg = list(jieba.cut(text, cut_all=False))
        return cn_seg
    except Exception as e:
        print('cn', e)
        return []


def calculate_tfidf(segmented_corpus):
   
