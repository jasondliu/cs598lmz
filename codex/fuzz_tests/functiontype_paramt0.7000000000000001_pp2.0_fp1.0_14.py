from types import FunctionType
list(FunctionType(user_function).__code__.co_varnames)

## 6. Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 7. Exploring built-in modules ##

import math
print(dir(math))

## 8. The CSV module ##

import csv
f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl = list(csvreader)

## 9. Counting how many times a team won ##

import csv
f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))
patriots_wins = 0
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1
        

## 10. Making a function that counts wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team):
