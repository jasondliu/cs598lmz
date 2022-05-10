import sys, threading

def run():
    while True:
        try:
            print('Введите номер вагона:')
            number = int(input())
            print('Введите тип вагона:')
            type = input()
            print('Введите количество мест:')
            seats = int(input())
            wagon = Wagon(number, type, seats)
            print(wagon)
        except ValueError:
            print('Неверный ввод')

class Wagon:
    def __init__(self, number, type, seats):
        self.number = number
        self.type = type
        self.seats = seats

    def __str__(self):
        return 'Вагон №{} типа {} с количеством мес
