import codecs
codecs.register_error("strict", codecs.ignore_errors)

def load_liwc_dict(path, exclusive_categories=("Numbers", "QMark")):
    liwc_regex_pattern = re.compile("\s*(\d+)\s+(.+)")
    liwc_dict = defaultdict(set)
    with open(path, 'r', encoding='UTF-8') as liwc_file:
        for line in liwc_file:
            match = re.match(liwc_regex_pattern, line)
            if match is not None:
                category = match[2]
                if category not in exclusive_categories:
                    word = match[1]
                    liwc_dict[word].add(category)
    return liwc_dict

def load_liwc_categories(path):
    liwc_regex_pattern = re.compile("\s*(\d+)\s+([^\*]+)\s*")
    liwc_categories = {}
    with open(path, 'r',
