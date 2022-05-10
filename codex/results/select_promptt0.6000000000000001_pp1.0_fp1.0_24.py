import select
# Test select.select()

def test1():
	print('\nSelect test 1')
	r = [sys.stdin]
	w = []
	x = []
	r, w, x = select.select(r, w, x)
	print('r =', r)
	print('w =', w)
	print('x =', x)

def test2():
	print('\nSelect test 2')
	r = []
	w = [sys.stdout]
	x = []
	r, w, x = select.select(r, w, x)
	print('r =', r)
	print('w =', w)
	print('x =', x)

def test3():
	print('\nSelect test 3')
	r = []
	w = []
	x = []
	r, w, x = select.select(r, w, x)
	print('r =', r)
	print('w =', w)
	print('x =', x)

def test4():
	print('\nSelect test 4')
