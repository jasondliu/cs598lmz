import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

cora_path = '../cora'
author_pub_dict = {}
author_num, paper_num = 0, 0
with open(cora_path + '/cora.content', 'r') as f:
    for line in f.readlines():
        paper_num += 1
        ls = line.split('\t')
        author_list = ls[3]
        author_list = author_list.split(';')
        author_list = [au_li.strip() for au_li in author_list if len(au_li) > 1]
        for author in author_list:
            if author not in author_pub_dict.keys():
                author_num += 1
                author_pub_dict[author] = [paper_num - 1]
            else:
                author_pub_dict[author].append(paper_num - 1)
print('Cora network initialized.')

with open(cora_path + 'cora
