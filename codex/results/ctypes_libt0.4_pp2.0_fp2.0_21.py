import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#Create a function that will return a list of all the numbers from 1 to 100 that are divisible by 3 and 7.

def divisibles():
    nums = []
    for i in range(1,101):
        if i%3 == 0 and i%7 == 0:
            nums.append(i)
    return nums

print(divisibles())

#Create a function that will return the number of vowels in a string.

def vowels(string):
    count = 0
    for i in string:
        if i in "aeiou":
            count += 1
    return count

print(vowels("hello"))

#Create a function that will return the number of words in a string.

def words(string):
    count = 1
    for i in string:
        if i == " ":
            count += 1
    return count

print(words("hello world"))

#Create a function that will return the number of words in a
