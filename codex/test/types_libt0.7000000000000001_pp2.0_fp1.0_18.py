import types
types.SimpleNamespace

from lib.maze import Maze
from lib.astar import Astar
from lib.qlearning import QLearning

def main():
    maze = Maze('maze.png')
    astar = Astar(maze)
    q_learning = QLearning(maze)

    # q_learning.train()
    # q_learning.test()

    astar.search()
    astar.test()

    # print(q_learning.Q)
    # print(q_learning.R)

if __name__ == '__main__':
    main()
