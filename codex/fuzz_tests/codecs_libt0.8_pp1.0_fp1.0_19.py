import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#Author: Alex Li
def get_data(fi,col):
    '''
    get the data from the file by column number
    '''
    f = open(fi)
    lines = f.readlines()
    f.close()
    lis = []
    for line in lines:
        line = line.strip()
        line = line.decode('gbk')
        line = line.encode('utf-8')
        line = line.strip('\"')
        l_list = line.split('\" \"')
        new_list = []
        for i in l_list:
            i = i.split('\t')
            new_list.append(i[col])
        lis.append(new_list)
    return lis

def count_data(lis):
    '''
    calculate the number of each data in lis
    '''
    result = {}
    for i in lis:
        if i
