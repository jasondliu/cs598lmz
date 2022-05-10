from types import FunctionType
list(FunctionType('equation', {})('x+2y-11=7', '-x+2y=2'))

def equation(equ1, equ2):
    sys = re.sub('=', '=s', equ1+equ2).replace('^', '').split('s')
    ex = list(set(set(sys[0]) | set(sys[1])) - {'+', '-', '='})[0]
    eq1 = [float(i.strip()) for i in re.sub(f"{ex}", '1', sys[0]).split('+')]
    eq2 = [float(i.strip()) for i in re.sub(f"{ex}", '1', sys[1]).split('+')]
    eq1.append(eq1.pop(0))
    eq2.append(eq2.pop(0))
    D = eq1[0] * eq2[1] - eq1[1] * eq2[0]
    Dy = eq1[2] * eq2[1] - eq1[1] * eq2
