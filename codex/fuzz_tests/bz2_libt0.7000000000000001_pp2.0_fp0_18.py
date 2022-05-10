import bz2
bz2.compress(b'hello world')

import random
random.randint(1, 10)
random.choice(['hello', 'hi', 'hey', 'howdy'])

import shelve

with shelve.open('mydata') as fruit:
    # fruit is a dictionnary
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

    fruit["lime"] = "great with tequila"

    for snack in fruit:
        print(snack + ": " + fruit[snack])

    while True:
        dict_key = input("Please enter a fruit: ")
        if dict_key == "quit":
            break

        if dict_key in fruit:
            description = fruit[dict_
