import ctypes
ctypes.windll.kernel32.SetConsoleMode(hstdout, immediate_write)

# https://www.hackerrank.com/challenges/two-strings

def contains_common_substring(a, b):
    """
    Find the common substring in the given strings
    """
    substring_counter = {}

    for char in a:
        if char in substring_counter:
            substring_counter[char] += 1
        else:
            substring_counter[char] = 1

    for char in b:
        if char in substring_counter:
            return "YES"

    return "NO"

def main():
    num_tests = int(input())

    while num_tests > 0:
        a = input()
        b = input()

        print(contains_common_substring(a, b))

        num_tests -= 1

if __name__ == "__main__":
    main()
