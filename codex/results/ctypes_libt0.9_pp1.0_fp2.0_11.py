import ctypes
ctypes.windll.user32.MessageBoxW(0, "Prediction Complete", "3rd Eye", 1)

import shelve
db= shelve.open("score.dat")
try:
# function in add_scores.py file is 'add_scores(name,score)'
	db["score"] = total
	db["label"] = encoded_label
finally:
	db.close()


print("Shelve File saved -> 'score.dat'")
