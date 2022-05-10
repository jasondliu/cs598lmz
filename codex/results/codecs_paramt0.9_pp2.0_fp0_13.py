import codecs
codecs.register_error('strict', codecs.ignore_errors)


def get_syllables():

    lines = [l.strip() for l in codecs.open('cmudict-0.7b.txt', 'r', 'latin-1', 'strict').readlines()]
    pro_splitter = re.compile('(?:(?:^| )[A-Z-]+\d+.*)+.+')
    word_splitter = re.compile('[\w]+')

    syl_dict = defaultdict(list)

    for line in lines:
        if not line:
            continue

        match_pronun = pro_splitter.match(line)

        if match_pronun:
            word = word_splitter.findall(line)[0]

            pro_split_1 = line.split('  ')
            pronun = pro_split_1[1]
            pro_split_2 = pronun.split(' ')

            for p in pro_split_2:
                if p.strip():
                    syl_dict[word].append(p
