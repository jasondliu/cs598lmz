import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def get_name(message):
    name=input(message)
    return name

def get_number(message):
    num=input(message)
    return num

def get_score(message):
    score=input(message)
    return score

def display_score(score):
    print("Your grade is: "+score)

def calc_grade(score):
    if score in range(90,101):
        grade="A"
    if score in range(80,90):
        grade="B"
    if score in range(70,80):
        grade="C"
    if score in range(60,70):
        grade="D"
    if score in range(0,60):
        grade="F"
    return grade


def main():
    print("Welcome to the Calculator")
    print("Please enter your name")
    name=get_name("Please enter your name: ")
    print("Please enter your number")
    number=get
