import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)

def infix_to_prefix(expression):
    stack1 = deque()
    stack2 = deque()
    for w in expression.split(" "):
        if w == "(":
            stack1.append(w)
        elif w == ")":
            while stack1 and stack1[-1] != "(":
                stack2.append(stack1.pop())
            stack1.pop()
        elif w in operators:
            while stack1 and stack1[-1] != "(" and operators[w][1] <= operators[stack1[-1]][1]:
                stack2.append(stack1.pop())
            stack1.append(w)
        else:
            stack2.append(w)
    while stack1:
        stack2.append(stack1.pop())
    return " ".join(stack2)


def calculate_prefix(expression):
    stack = deque()
    for w in expression.split(" "):
        if w in
