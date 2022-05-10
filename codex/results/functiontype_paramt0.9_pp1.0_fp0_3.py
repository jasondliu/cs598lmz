from types import FunctionType
list(FunctionType().__dict__.keys())[:10]

doc=FunctionType.__doc__
'lala' in doc
'>>> ok'
'return lala'

doc.find('lala')
import time
time.__doc__


l=['a']
l.__contains__('a')

len.__doc__
'''
Return the number of items in a container.
'''



def test_lambda(lamba1, lambda2=time.clock):
    def test_func(a):
        lamba1(a/10)
        lambda2(a/10)
    return test_func

test_lambda(time.sleep, time.ctime)(1)




lals=[]
def su(a):
    gs=globals()
    for s in gs:
        try:
            if 'lals' == s:
                continue
            if a in gs[s]:
                lals.append(s)
        except Exception:
            continue

if __name__ == "__main__":
    import
