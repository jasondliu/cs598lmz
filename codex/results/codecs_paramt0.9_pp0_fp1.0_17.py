import codecs
codecs.register_error('ignore', codecs.lookup_error(encoding='ascii'))
def read_lst(fn_lst, f_key="name", str_key = "Name"):
    lst = []
    with codecs.open(fn_lst, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            lst.append(line)
                        
    return lst

def write_lst(lst, fmt="%s", fn_out=None):
    if fn_out is None:
        fn_out = "%s.lst" % time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    with codecs.open(fn_out,"w",encoding="utf-8") as fout:
        for e in lst:
            fout.write(fmt % e)
            fout.write("\n")

if __name__ == "__main__":
   
