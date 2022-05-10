import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))
import sys

def set_txt(text):
    global txt
    txt = text

def get_txt():
    return txt

def get_lst(file_name):
    lst = []
    try:
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                lst.append(line)
    except:
        print(file_name + " is not exist!")
        sys.exit(0)
    return lst

def get_dic(file_name):
    dic = {}
    try:
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                dic[line] = 0
    except:
        print(file_name + " is not exist!")
        sys.exit(0)
    return dic

def get_str(file_name
