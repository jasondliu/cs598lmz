import ctypes
ctypes.cast(id(0), ctypes.py_object).value

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif s[i] == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif s[i] == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(
