import types
# Test types.FunctionType
def test(expected, func):
    if func is None or type(func) != types.FunctionType:
        return False
    else:
        return func(expected)
# Refine to the user input.
print("Please input you choice(1 or 2)")
number = input()
if number == '1':
    check = lambda x:x
elif number == '2':
    check = lambda x:not x
else:
    print("Invalid input.")
    exit()

# Binary search.
lower = -1
upper = 1000
while upper - lower > 1:
    middle = (lower + upper) // 2
    print("Is your secret number " + str(middle) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    feedback = input()
    if feedback == 'h':
        if check(test(middle, is_too_high)):
            upper = middle
        else:
            print("Sorry, your input is invalid.")
           
