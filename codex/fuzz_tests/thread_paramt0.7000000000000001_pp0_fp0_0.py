import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

class Question:
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def ask(self):
        print("\n" + self.question)
        self.print_choices()
        self.read_answer()
        self.evaluate()

    def print_choices(self):
        for choice in self.choices:
            print("(" + choice + ")", self.choices[choice])

    def read_answer(self):
        self.userAnswer = input("Your answer: ")

    def evaluate(self):
        if self.userAnswer == self.answer:
            print("Correct!")
        else:
            print("Incorrect! The answer was: " + self.answer)
            raise Exception("Incorrect answer")

# Question 1
question1 = Question("What is the name of the world's largest ocean?", "Pacific Ocean", {
    "a": "Pacific Ocean",
    "b": "Indian Ocean",
