import types
types.SimpleNamespace(**{'cmd': 'patch', 'input': "../inputs/maze3.txt", 'output': sys.stdout, 'n': '2 2', 'maze': [[1, 0], [0, 1]]})

# cmd: option
# input: file
# output: sys.stdout
# maze: list
# n, m: str
" ".join(["python3", "benchmark.py", "--cmd", "patch", "--input", "../inputs/maze3.txt", "--n", "2", "2", "--ns", "NaN"])

# Give 'maze'
# Output maze, (n,m)
import puzzle_main
puzzle_main.dimen_transform(maze)

# Give (n,m)
# Output maze
import puzzle_main
str_maze = puzzle_main.parse_raw(args.maze, args.n, args.m)
import puzzle_main
print(puzzle_main.pretty_print(str_maze))


string = "1231243
