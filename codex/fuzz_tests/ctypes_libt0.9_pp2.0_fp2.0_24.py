import ctypes
ctypes.cdll.LoadLibrary('./solution.so')
import solution

s = '''
{{{([])[()]}}}

{{()[]}}{}

{}([])
'''

s = s.split('\n')

for i in s:
    print(solution.isBalanced(i))


#print(solution.isBalanced('{{{([])[()]}}}'))
#print(solution.isBalanced('{{()[]}}{}'))
#print(solution.isBalanced('{}([])'))
