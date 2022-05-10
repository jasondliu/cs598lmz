import threading
threading.stack_size(52428800)

#
# Define the problem
#
class ProblemInstance:
    def __init__(self):
        self.numVars = 2
        self.varSize = [8,8]
        self.domain = [[(0,1)]*self.varSize[i] for i in range(self.numVars)]
        random.seed(1)
        self.codomain = [0]*self.varSize[0]
        for i in range(self.varSize[0]):
            self.codomain[i] = random.randint(0,1)
        self.numTests = 10
        self.tests = []
        for i in range(self.numTests):
            testInput = [0]*self.varSize[0]
            for j in range(self.varSize[0]):
                testInput[j] = random.randint(0,1)
            testOutput = 0
