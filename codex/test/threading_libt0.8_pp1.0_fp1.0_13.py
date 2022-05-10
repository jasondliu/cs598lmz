import threading
threading.stack_size(2**27)  # Increase stack size to allow large recursion


def isBalanced(s):
    # [int] -> bool
    # rtype: bool
    """
    Return whether a string of parentheses, curly braces, and square
    brackets is balanced.
    """
    stack = []

    pairs = {'(': ')',
             '{': '}',
             '[': ']'}

    for c in s:
        if c in pairs:
            stack.append(pairs[c])
        else:
            if stack == [] or stack.pop() != c:
                return False
    return stack == []


def main():
    T = int(input().strip())
    for a0 in range(T):
        s = input().strip()
        if isBalanced(s):
            print('YES')
        else:
            print('NO')


threading.Thread(target=main).start()
