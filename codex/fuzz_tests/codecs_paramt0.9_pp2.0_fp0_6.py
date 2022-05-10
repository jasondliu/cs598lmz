import codecs
codecs.register_error("strict", codecs.ignore_errors)

def loadLexicon(fname):
    newLex=set()
    lex_conn=codecs.open(fname,mode='r',encoding='utf-8')
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def cmp_lex(l1,l2):
    t1=l1.split('-')
    t2=l2.split('-')
    w1=t1[0]
    w2=t2[1]

    l1=set(l1.split('-'))
    l2=set(l2.split('-'))
    a=l1.difference(l2)
    b=l2.difference(l1)
    if len(a)==0 and len(b)==0:
        return True
    else:
        return False

def findLexicon(yelp_reference,bd_lexicon
