import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'))


def get_data(file_path, predicate_path=None, is_test=False, gold_path=None):
    """
    处理数据
    """
    print('Getting data...')
    data = []
    data_id_list = []
    query_p_map = {}
    with open(predicate_path, encoding='utf-8') as pf:
        for line in pf:
            line = line.strip().split()
            query_p_map[line[0]] = line[1]
    with open(file_path, encoding='utf-8') as f:
        for line in tqdm(f):
            # 如果存在谓词
            if predicate_path:
                lin = line.split('\t')
                query, sentence = lin[0], lin[1]
                query_p = query_p_map[query] if query in query_p_map else ''
                #
