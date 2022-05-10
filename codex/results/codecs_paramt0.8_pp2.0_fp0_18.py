import codecs
codecs.register_error('replace_latin_u', lambda e: (u'\ufffd', e.start + 1))


def main():
    #第一步 读取文件
    #read_file_name = unicode(sys.argv[1], 'utf-8')
    #read_file_encoding = sys.argv[2]
    #read_file = codecs.open(read_file_name, 'r', encoding=read_file_encoding)
    #read_file = codecs.open('/home/viki/Downloads/work/fc/f_candidate_relation_dict', 'r', encoding='utf-8')
    read_file = codecs.open('/home/viki/Downloads/work/fc/f_candidate_relation_dict_level_1', 'r', encoding='utf-8')
    
    #第二步 建立输出数据容器
    out_relation_dict = {}
    
    #第
