import select_row
import select_col
import select_box
import select_value
import solve
import print_sudoku
import input_sudoku
import write_sudoku

# =============================================================================
# Main function
# =============================================================================
# Define a sudoku as a list of lists, each containing the values of the rows.
# A zero indicates a missing value.
sudoku = []
# Load a sudoku from a file.
sudoku = input_sudoku.input_sudoku()
# Print the sudoku.
print_sudoku.print_sudoku(sudoku)
# Solve the sudoku by trying to select a value in each row, then column and
# then box.
solved = solve.solve(sudoku)
# Print the solved sudoku.
print_sudoku.print_sudoku(solved)
# Write the solved sudoku to a file.
write_sudoku.write_sudoku(solved)
