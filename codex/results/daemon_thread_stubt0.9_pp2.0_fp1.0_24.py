import sys, threading

def run():
	call(["psql", "-f","../sql/hr.sql"])
	#call(["psql", "-f","../sql/query_functions.sql"])
	#call(["psql", "-f","../sql/test.sql"])
	print "Running query 1"
	call(["time","psql","-f","query1.sql"])
	print "Running query 2"
	call(["time","psql","-f","query2.sql"])
	print "Running query 3"
	call(["time","psql","-f","query3.sql"])
	print "Running query 4"
	call(["time","psql","-f","query4.sql"])
	print "Running query 5"
	call(["time","psql","-f","query5.sql"])
	print "Running query 6"
	call(["time","psql","-f","query6.sql"])
	print "Running query 7"
	call(["time","psql","-f","query7.sql"])
	print "Running
