import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in m:
                top_element = stack.pop() if stack else '#'
                if m[char] != top_element:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
