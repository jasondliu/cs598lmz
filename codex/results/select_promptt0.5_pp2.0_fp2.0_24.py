import select
# Test select.select()
#
# This is a test script for select.select(). It takes four arguments:
#
# - The name of the input file (a text file)
# - The name of the output file
# - The name of the error file
# - The amount of time to wait before timing out
#
# The script opens the three files and calls select.select() on them,
# with the specified timeout. If the call returns three empty lists,
# the script exits with a failure. Otherwise, it exits with success.
#
# Example usage:
#
#   $ python select_echo.py to_be_copied.txt copied.txt /dev/null 5
#
# This script can be used to test the timeout feature of select.select().
#
#   $ python select_echo.py to_be_copied.txt copied.txt /dev/null 5
#   select() returned ([], [], []) before timeout
#   $ echo $?
#   1
#   $ python select_echo.py to_be_copied.txt copied.txt /dev/null 500
#   select() returned
