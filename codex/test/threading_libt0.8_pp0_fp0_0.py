import threading
threading.stack_size(2147480000)
sys.setrecursionlimit(2147480000)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    table[i][j] = grid[i][j]
                elif i == 0:
                    table[i][j] = grid[i][j] + table[i][j - 1]
                elif j == 0:
                    table[i][j] = grid[i][j] + table[i - 1][j]
                else:
                    table[i][j] = grid[i][j] + min(table[i - 1][j], table[i][j - 1])
        return table[len(grid) - 1][len(grid[0]) - 1]


