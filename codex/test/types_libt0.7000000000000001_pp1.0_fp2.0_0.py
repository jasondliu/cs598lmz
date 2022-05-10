import types
types.FunctionType

type(lambda x: x)

type(type(42))

type(type(int))

def check_coffee_stock(func):
    def wrapper():
        if 'coffee' not in stock:
            print('oops! out of coffee')
            return None
        return func()
    return wrapper

def restock_coffee():
    stock['coffee'] += 300

stock = {'coffee': 100}

restock_coffee()

check_coffee_stock(restock_coffee)()

def check_coffee_stock(func):
    def wrapper():
        if 'coffee' not in stock:
            print('oops! out of coffee')
            return None
        return func()
    return wrapper

@check_coffee_stock
def restock_coffee():
    stock['coffee'] += 300

stock = {'coffee': 100}

restock_coffee()

