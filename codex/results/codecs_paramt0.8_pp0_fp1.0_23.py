import codecs
codecs.register_error('surrogateescape', codecs.escape_decode)

from gensim.corpora import WikiCorpus

"""
    讲wiki的xml文件转化为txt文件
    :param in_f: wiki的xml文件
    :param out_f: 输出文件
"""
def wiki_to_txt(in_f, out_f):
    # 生成经过分词之后的txt文件
    wiki_corpus = WikiCorpus(in_f, lemmatize=False, dictionary={})
    texts_num = 0

    with codecs.open(out_f, 'w', encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logger.info("已處理 %d 篇
