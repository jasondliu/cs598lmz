import types
types.NoneType#odasłanie czegoś co jest w niektórej wersji Pythona
import math

def zbuduj (L, R, N, puncta):
	lewa, prawa, dolna, gorna, rysujemy = L, R, dol + (gora-dol) / float(N), gora, False
	for x in range(N):
		for i in range(len(puncta)):
			x1, y1 = puncta[i]
			if y1 <= gorna and y1 >= dolna:
				rysujemy = True
				if x1 <= lewa or x1 >= prawa:
					rysujemy = False
					break
		#rysuj
