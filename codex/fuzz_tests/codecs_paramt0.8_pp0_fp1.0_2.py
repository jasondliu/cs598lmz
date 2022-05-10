import codecs
codecs.register_error('empty', codecs.replace_errors('ignore'))

def stopwords(swfile):
    with codecs.open(swfile, encoding='utf-8', mode='r') as swfile2:
        sw = swfile2.read().split('\n')
    return sw

def linefile(txtfile, sw):
    with codecs.open(txtfile, encoding='utf-8', mode='r') as txtfile2:
        lines = txtfile2.read().split('\n')
    linere = re.compile('^\d+\t')
    nlst = []
    for line in lines:
        if line and linere.match(line):
            nlst.append(line.split('\t'))
    return nlst

def getnums(line, sw):
    numre = re.compile('[0-9]+')
    nums = []
    for word in line:
        if word not in sw and numre.search(word):
            nums.append(word)
    return nums

