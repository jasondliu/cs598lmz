from types import FunctionType
list(FunctionType(triple_concat_encode, {}).parameters.values())[1].default

class Problem:
    def __init__(self, N, a, b, c):
        self.N = N
        self.a = a
        self.b = b
        self.c = c
        self.solution_found = False

    @property
    def in_range(self):
        return 1 <= self.N <= 10 ** 10 ** 5

    def solve(self):
        self.solution_found = False

        f = triple_concat_encode
        
        solved_triples = set()
        
        for x in range(1, self.N + 1):
            for y in range(1, self.N + 1):
                for z in range(1, self.N + 1):
                    if (
                        (x * y * z) % self.N == 0 and
                        f(x, self.a) == f(y, self.b) == f(z, self.c)
                    ):
                        solved_triples.add((x,
