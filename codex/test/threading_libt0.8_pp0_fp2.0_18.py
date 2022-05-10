import threading
threading.stack_size(200000000)

def main():
	t3 = time.time()
	path = "./data/movies_large.dat"
	movies = loadMovies(path)
	t4 = time.time() - t3
