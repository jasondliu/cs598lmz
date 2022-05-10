import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Sudoku Solver")

#Function for printing the grid
def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()

#Function for checking if the grid is full or not
def check_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return False
    return True

#Function for finding the next empty cell
def find_next(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j

#Function for checking if the number is valid in the row
def check_row(grid,row,num):
    for i in range(9):
        if grid[row][i]==num:
            return False
    return True

#Function for checking if the number is valid in the column
def check_
