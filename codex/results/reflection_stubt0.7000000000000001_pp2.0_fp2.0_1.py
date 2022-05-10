fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def get_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

#https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
def false_positive(lst):
    return [i for i in lst if type(i) == bool and i == False]

#https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

#https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
def opposite(number):
    return -number
