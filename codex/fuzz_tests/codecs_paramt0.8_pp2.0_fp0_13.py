import codecs
codecs.register_error('strict', codecs.ignore_errors)

class CnConv:
    """
    This is the docstring.
    """
    def __init__(self):
        self.zhcn = self.loadZhcn()
        self.zhtw = self.loadZhtw()
        self.quickFull = self.loadQuickFull()

    def loadQuickFull(self):
        cn_full = {}
        cn_quick = {}

        with codecs.open('./dict/zh-cn_full.txt', 'r', 'utf-8', 'strict') as f:
            for line in f.readlines():
                if line is not None:
                    pair = line.strip().split(' ')
                    cn_full[pair[0]] = pair[1]
                    cn_quick[pair[0][0:1]] = pair[1]

        return [cn_full, cn_quick]

    def loadZhcn(self):
        zhcn = []

        with codecs.open('./dict/zh-cn.txt
