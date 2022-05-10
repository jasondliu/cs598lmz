import select_functions
import math
import numpy
import matplotlib.pyplot as plt

# Select T2, T3, T4, T5, T6, T7, T8 from the database

db = MySQLdb.connect(host="localhost", user="root", passwd="mysql", db="movies")
cursor = db.cursor()

cursor.execute("SELECT T2, T3, T4, T5, T6, T7, T8 FROM movielens_ratings")

numrows = int(cursor.rowcount)

T2 = []
T3 = []
T4 = []
T5 = []
T6 = []
T7 = []
T8 = []

for x in range(0,numrows):
    row = cursor.fetchone()
    T2.append(row[0])
    T3.append(row[1])
    T4.append(row[2])
    T5.append(row[3])
    T6.append(row[4])
    T7.append(row
