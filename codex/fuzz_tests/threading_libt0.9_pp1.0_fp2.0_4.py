import threading
threading.stack_size(67108864) # 64MB stack
# threading.stack_size(2048000000)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        index = 0
        result = []
        for x in A:
            if x == B:
                result.append(index)
            index += 1
        return result
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        pos = {x: i for i, x in enumerate(A)}
        return [pos[x] for x in B]

    def findIndices(self, arr, value, indextofind):
        """
        :param arr: array of integers to search from
        :param value: integer value to search
        :param indextofind: 0 for first index and 1 for last index
        :return: returns first or last index of element in
