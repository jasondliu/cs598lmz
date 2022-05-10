import weakref

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


class JointSegment:
    def __init__(self,name,class_names,class_probs,th=0.02,minimum=2):
        self.name = name
        self.classes = class_names
        self.probs = class_probs
        self.th = th        
        self.minimum = minimum
        self.candidates = []
        self.text = defaultdict(list)
        self.prob = defaultdict(list)
        self.lineage = []
        self.start = defaultdict(list)
        self.stop = defaultdict(list)
        
    def get_prob(self,clas):

