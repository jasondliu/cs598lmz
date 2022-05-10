import codecs
codecs.register_error('replace_space', codecs.replace_errors(u' '))

class Replacer(object):
    def __init__(self, rules):
        self._rules = rules

    def __call__(self, word):
        return self._rules.get(word, word)

class RuleSet(object):
    def __init__(self, fname):
        self._rules = {}
        with codecs.open(fname, encoding='utf-8-sig', errors='replace_space') as f:
            for line in f:
                source, target = line.rstrip().split('\t')
                self._rules[source] = target

    def __call__(self, word):
        return self._rules[word]

def replace(word, rules):
    return rules(word)

def main(args):
    rules = RuleSet(args.rules)
    segs_in = codecs.open(args.segmented, encoding='utf-8-sig', errors='replace_space')
    segs_out = codecs.open(args.
