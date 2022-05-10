import _struct

class Problem:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        with open(self.filename) as f:
            self.count = int(f.readline())
            self.data = [list(map(int, line.split())) for line in f.readlines()]

    def calculate(self):
        self.result = 0

        for line in self.data:
            line.sort()
            self.result += line.pop() - line.pop(0)

        return self.result

    def solve(self):
        self.load_data()
        print(self.calculate())

if __name__ == '__main__':
    problem = Problem(sys.argv[1])
    problem.solve()
