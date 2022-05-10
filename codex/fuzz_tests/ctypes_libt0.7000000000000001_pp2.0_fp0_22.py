import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Maze Generator")

import curses
import time

stdscr = curses.initscr()
n = int(input("Size of maze: "))

maze = [[1]*(2*n+1) for i in range(n)]

visited = [[0]*n for i in range(n)]

def dfs(x, y):
    visited[y][x] = 1
    maze[y][2*x] = 0
    maze[y][2*x+1] = 0
    if x + 1 < n and visited[y][x+1] == 0:
        maze[y][2*x+2] = 0
        dfs(x+1, y)
    if y + 1 < n and visited[y+1][x] == 0:
        maze[y+1][2*x] = 0
        dfs(x, y+1)
    if x > 0 and visited[y][x-1] == 0:
        maze[y][2*x-2] = 0
