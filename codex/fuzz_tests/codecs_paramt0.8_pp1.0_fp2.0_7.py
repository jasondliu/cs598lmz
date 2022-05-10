import codecs
codecs.register_error('strict', codecs.ignore_errors)
def csv_to_dict(csv_iterator):
    header = True
    header_dict = {}
    for line in csv_iterator:
        # Skip header
        if header:
            for i, v in enumerate(line):
                v = v.decode("utf-8", "strict").lower()
                header_dict[v] = i
                # print(v, i)
            header = False
            continue
        # Make dictionary
        line_dict = {}
        for k, v in header_dict.items():
            line_dict[k] = line[v]
        yield line_dict

def get_f_score(p, r):
    if p + r < sys.float_info.epsilon:
        return 0
    return 2 * p * r / (p + r)
        
def evaluate(corpus, truth):
    truth = truth
    total = 0
    correct = 0
    correct_corrector = 0
    correct_correctee = 0
    found = 0
   
