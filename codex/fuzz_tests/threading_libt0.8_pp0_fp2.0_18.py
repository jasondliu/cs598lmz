import threading
threading.stack_size(200000000)

def main():
	t3 = time.time()
	path = "./data/movies_large.dat"
	movies = loadMovies(path)
	t4 = time.time() - t3
	print "Movies loaded in %.2f seconds" %t4
	
	path = "./data/ratings_large.dat"
	ratings = loadRatings(path)
	t5 = time.time() - t4 - t3
	print "Ratings loaded in %.2f seconds" %t5
	
	users = buildUsers(ratings)
	t6 = time.time() - t5 - t4 - t3
	print "Users built in %.2f seconds" % t6

	movies_rated_list = buildMoviesRatedList(ratings)
	t7 = time.time() - t6 - t5 - t4 - t3
	print "Movies Rated listed built in %.2f seconds" % t7
	
	movies_rated_list_2 = build
