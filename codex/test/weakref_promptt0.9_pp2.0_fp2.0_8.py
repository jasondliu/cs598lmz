import weakref
# Test weakref.ref()().
if __name__ == "__main__":
	a = b = [1]
	weakref.ref(a)()
	weakref.ref(b)()

	success
